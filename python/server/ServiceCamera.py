#!/usr/bin/env python
#-*- coding:utf-8 -*- 
import cv2
from include import *
from Msg import Msg

from ModelTurn import ModelTurn
from ModelMove import ModelMove
from cvhelp import CvHelp
from RtmpUtil import RtmpUtil

@singleton
class ServiceCamera:
    """ 
        Service 
        管理摄像头 识别opencv 判断处理 发送监控提醒socket推送
    """ 
    def __init__(self, serverSocket):
        self.ifRtmpPush = "0"
        self.serverSocket = serverSocket    # 通过此来推送关键消息
        return
    def doMethod(self, method, params):
        # params = params.encode('utf-8')
        # method = method.encode('utf-8')

        # tool.doMethod(self, method, params)
        print("class:  " + self.__class__.__name__)    #className
        print("method: " + method)    #list
        print("params: " + params)    #{arg1: 'a1', arg2: 'a2' }
        #检查成员
        ret = hasattr(self, method) #因为有func方法所以返回True 
        if(ret == True) :
            #获取成员
            method = getattr(self, method)#获取的是个对象
            return method(params) 
        else :
            print("Error ! 该方法不存在")
            return ""


# 开启摄像头监控识别
    def start(self):
        mycv = CvHelp()
    
        rtmp = RtmpUtil('rtmp://39.107.26.100:1935:1935/myapp/test1')
        camera = cv2.VideoCapture("test2.mp4") # 从文件读取视频

        # camera = cv2.VideoCapture(0) # 参数0表示第一个摄像头 摄像头读取视频
        # if (camera.isOpened()):# 判断视频是否打开 
        #     print 'Open camera'
        # else:
        #     print 'Fail to open camera!'
        #     return
        # camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 2560x1920 2217x2217 2952×1944 1920x1080
        # camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        # camera.set(cv2.CAP_PROP_FPS, 5)

        # 视频属性
        size = (int(camera.get(cv2.CAP_PROP_FRAME_WIDTH)), int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        fps = camera.get(cv2.CAP_PROP_FPS)  # 30p/self
        fps = int(fps)
        hz = int(1000.0 / fps)
        print 'size:'+repr(size) + ' fps:' + str(fps) + ' hz:' + str(hz)

        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('res_mv.avi',fourcc, fps, size)
        lineWidth = 1 + int((size[1]-400) / 400)# 400 1 800 2 1080 3
        textSize = size[1] / 1000.0# 400 0.45 
        heightDeta = size[1] / 20 + 10# 400 20
        count = 0
        faces = []
        while True:
            ###########################图片采集
            count = count + 1
            ret, frame = camera.read() # 逐帧采集视频流
            if not ret:
                break

            if(count % 1 == 0):
            ###########################图片处理
                # 探测图片中的人脸 延帧检测
                faces = mycv.classfier.detectMultiScale(frame,scaleFactor=1.1,minNeighbors=5,minSize=(5,5))
                pass
            for (x, y, w, h) in faces:
                # cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                mycv.drawRect(frame, (x, y), (x+w, y+h), (128, 64, 255), line_width=lineWidth )

            # print(len(faces))
            fpsshow = "Fps  :" + str(int(fps)) + "  Frame:" + str(count)  
            nframe  = "Play :" + str(int(count / fps))
            ntime   = "Time :" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if(count % fps == 0):
                print(fpsshow + " " + ntime)
            mycv.drawText(frame, (0, heightDeta), fpsshow, textSize=textSize, lineWidth=lineWidth )
            mycv.drawText(frame, (0, heightDeta * 2), nframe, textSize=textSize, lineWidth=lineWidth )
            mycv.drawText(frame, (0, heightDeta * 3), ntime, textSize=textSize, lineWidth=lineWidth )

            ############################图片输出
            # 结果帧处理 存入文件 / 推流 / ffmpeg 再处理
            out.write(frame)
            rtmp.write(frame.tostring())

            # if cv2.waitKey(1) & 0xFF == ord('q'):
            #     break
            # cv2.waitKey(hz)
            if(count > fps * 10):
                break;
        camera.release()
        # Release everything if job is finished
        out.release()
        print("Over!")
        pass

# 关闭监控识别
    def stop(self):
        passwd

# 开启推送视频
    def openPush(self):
        self.ifRtmpPush = "1"
# 关闭推送视频
    def closePush(self):
        self.ifRtmpPush = "0"




 
    def toString(self):
        res = "" 

        return res


if __name__ == '__main__':
    serviceCamera = ServiceCamera(1)

    serviceCamera.start()
