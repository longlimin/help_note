# -- coding: utf-8 --
# http://blog.csdn.net/luhanglei
import time
import traceback
import ctypes
from librtmp import *



class RtmpUtil():  # camera可以通过一个类文件的对象来输出，实现write方法即可
    conn = None  # rtmp连接
    sps = None  # 记录sps帧，发过以后就不需要再发了（抓包看到ffmpeg是这样的）
    pps = None  # 同上
    sps_len = 0  # 同上
    pps_len = 0  # 同上

    time_stamp = 0

    def __init__(self):

        self.conn = RTMP( 'rtmp://192.168.199.154/oflaDemo/test', live=True)
        librtmp.RTMP_EnableWrite(conn.rtmp)
        self.conn.connect()
        self.start_time = time.time()
        # 拼装视频格式的数据包
        self.meta_body_array = [get_meta_string('@setDataFrame'), get_meta_string('onMetaData'),
                           bytes(bytearray([0x08, 0x00, 0x00, 0x00, 0x06])),  # 两个字符串和ECMA array头，共计6个元素,注释掉了音频相关数据
                           self.get_property_string('width'), self.get_meta_double(640.0),
                           self.get_property_string('height'), self.get_meta_double(480.0),
                           self.get_property_string('videodatarate'), self.get_meta_double(0.0),
                           self.get_property_string('framerate'), self.get_meta_double(25.0),
                           self.get_property_string('videocodecid'), self.get_meta_double(7.0),
                           # get_property_string('audiodatarate'), get_meta_double(125.0),
                           # get_property_string('audiosamplerate'), get_meta_double(44100.0),
                           # get_property_string('audiosamplesize'), get_meta_double(16.0),
                           # get_property_string('stereo'), get_meta_boolean(True),
                           # get_property_string('audiocodecid'), get_meta_double(10.0),
                           self.get_property_string('encoder'), self.get_meta_string('Lavf57.56.101'),
                           bytes(bytearray([0x00, 0x00, 0x09]))
                           ]
        self.meta_body = ''.join(meta_body_array)
        print ("meta_body : " + str(self.meta_body.encode('hex')))
        self.meta_packet = RTMPPacket(type=PACKET_TYPE_INFO, format=PACKET_SIZE_LARGE, channel=0x04, timestamp=0, body=meta_body)
        self.meta_packet.packet.m_nInfoField2 = 1  # 修改stream id
        self.stream = conn.create_stream(writeable=True)

        # with picamera.PiCamera() as camera:
        #     camera.start_preview()
        #     time.sleep(2)
        #     camera.start_recording(Writer(conn), format='h264', resize=(640, 480), intra_period=25,
        #                            quality=25)  # 开始录制，数据输出到Writer的对象里
        #     while True:#永远不停止
        #         time.sleep(60)
        #     camera.stop_recording()
        #     camera.stop_preview()


    def write(self, data):
        try:
            # 寻找h264帧间隔符
            indexs = []
            index = 0
            data_len = len(data)
            while index < data_len - 3:
                if ord(data[index]) == 0x00 and ord(data[index + 1]) == 0x00 and ord(
                        data[index + 2]) == 0x00 and ord(data[index + 3]) == 0x01:
                    indexs.append(index)
                    index = index + 3
                index = index + 1
            # 寻找h264帧间隔符 完成
            # 通过间隔符个数确定类型，树莓派摄像头的第一帧是sps+pps同时发的
            if len(indexs) == 1:  # 非sps pps帧
                buf = data[4: len(data)]  # 裁掉原来的头（00 00 00 01），把帧内容拿出来
                buf_len = len(buf)
                type = ord(buf[0]) & 0x1f
                if type == 0x05:  # 关键帧，根据wire shark抓包结果，需要拼装sps pps 帧内容 三部分，长度都用4个字节表示
                    body0 = 0x17
                    data_body_array = [bytes(bytearray(
                        [body0, 0x01, 0x00, 0x00, 0x00, (self.sps_len >> 24) & 0xff, (self.sps_len >> 16) & 0xff,
                         (self.sps_len >> 8) & 0xff,
                         self.sps_len & 0xff])), self.sps,
                        bytes(bytearray(
                            [(self.pps_len >> 24) & 0xff, (self.pps_len >> 16) & 0xff, (self.pps_len >> 8) & 0xff,
                             self.pps_len & 0xff])),
                        self.pps,
                        bytes(bytearray(
                            [(buf_len >> 24) & 0xff, (buf_len >> 16) & 0xff, (buf_len >> 8) & 0xff, (buf_len) & 0xff])),
                        buf
                    ]
                    mbody = ''.join(data_body_array)
                    time_stamp = 0  # 第一次发出的时候，发时间戳0，此后发真时间戳
                    if self.time_stamp != 0:
                        time_stamp = int((time.time() - start_time) * 1000)
                    packet_body = RTMPPacket(type=PACKET_TYPE_VIDEO, format=PACKET_SIZE_LARGE, channel=0x06,
                                             timestamp=time_stamp, body=mbody)
                    packet_body.packet.m_nInfoField2 = 1
                else:  # 非关键帧
                    body0 = 0x27
                    data_body_array = [bytes(bytearray(
                        [body0, 0x01, 0x00, 0x00, 0x00, (buf_len >> 24) & 0xff, (buf_len >> 16) & 0xff,
                         (buf_len >> 8) & 0xff,
                         (buf_len) & 0xff])), buf]
                    mbody = ''.join(data_body_array)
                    # if (self.time_stamp == 0):
                    self.time_stamp = int((time.time() - start_time) * 1000)
                    packet_body = RTMPPacket(type=PACKET_TYPE_VIDEO, format=PACKET_SIZE_MEDIUM, channel=0x06,
                                             timestamp=self.time_stamp, body=mbody)
                self.conn.send_packet(packet_body)
            elif len(indexs) == 2:  # sps pps帧
                if self.sps is not None:
                    return
                data_body_array = [bytes(bytearray([0x17, 0x00, 0x00, 0x00, 0x00, 0x01]))]
                sps = data[indexs[0] + 4: indexs[1]]
                sps_len = len(sps)
                pps = data[indexs[1] + 4: len(data)]
                pps_len = len(pps)
                self.sps = sps
                self.sps_len = sps_len
                self.pps = pps
                self.pps_len = pps_len
                data_body_array.append(sps[1:4])
                data_body_array.append(bytes(bytearray([0xff, 0xe1, (sps_len >> 8) & 0xff, sps_len & 0xff])))
                data_body_array.append(sps)
                data_body_array.append(bytes(bytearray([0x01, (pps_len >> 8) & 0xff, pps_len & 0xff])))
                data_body_array.append(pps)
                data_body = ''.join(data_body_array)
                body_packet = RTMPPacket(type=PACKET_TYPE_VIDEO, format=PACKET_SIZE_LARGE, channel=0x06,
                                         timestamp=0, body=data_body)
                body_packet.packet.m_nInfoField2 = 1

                self.conn.send_packet(meta_packet, queue=True)
                self.conn.send_packet(body_packet, queue=True)
        except Exception, e:
            traceback.print_exc()

    def flush(self):
        pass


    def get_property_string(self, string):  # 返回两字节string长度及string
        length = len(string)
        return ''.join([chr((length >> 8) & 0xff), chr(length & 0xff), string])


    def get_meta_string(self, string):  # 按照meta packet要求格式返回bytes,带02前缀
        return ''.join([chr(0x02), self.get_property_string(string)])


    def get_meta_double(self, db):
        nums = [0x00]
        fp = ctypes.pointer(ctypes.c_double(db))
        cp = ctypes.cast(fp, ctypes.POINTER(ctypes.c_longlong))
        for i in range(7, -1, -1):
            nums.append((cp.contents.value >> (i * 8)) & 0xff)
        return ''.join(bytes(bytearray(nums)))


    def get_meta_boolean(self, isTrue):
        nums = [0x01]
        if (isTrue):
            nums.append(0x01)
        else:
            nums.append(0x00)
        return ''.join(bytes(bytearray(nums)))

