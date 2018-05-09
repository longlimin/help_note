#!/usr/bin/env python
#-*- coding:utf-8 -*-  
from include import *
import threading
import json
import thread
import socket
import struct
import yaml
from Msg import Msg
########################################
from ServiceServer import ServiceServer

############################



@singleton
class ServerSocket:
    _socket_thread_read = 1
    client = {}
    _head_size = 4
    maxReadLen = 1024        #一次性读取最大长度
    threadReadDeta = 0.05    #无数据时读取间隔s
    threadReturnDeta = 1    #异常恢复间隔s

    # 监听消息
    def threadReadRun(self):

        while(1):
            print("threadReadRun start")
            while (self._socket_thread_read):
                jsonstr = self.readImpl(self.client)
                if(jsonstr):
                    self.onReceive(jsonstr)
                time.sleep(self.threadReadDeta)
            print("threadReadRun stop")
            time.sleep(self.threadReturnDeta)
    # 实现控制台输入推送消息
    def threadInputRun(self):

        threadInputCount = 0
        while(True):
            print("threadInputRun start" + str(threadInputCount))

            # 能发送前先 认证系统
            self.loginOn(self.client)

            while (self._socket_thread_read):
                cmd=raw_input("Input words to broadcast:")
                msg = Msg()
                msg.msgType = -2        #广播所有 测试用
                msg.data = {"broadcast":cmd}
                # print("make", jsonstr)
                self.sendImpl(msg.toString())
                time.sleep(self.threadReadDeta)
            print("threadInputRun stop" + str(threadInputCount))
            threadInputCount = threadInputCount + 1
            time.sleep(self.threadReturnDeta)


    # 链接服务器中转站
    def start(self, ip, port):
        print("Start client socket")
        self.client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
        
        reconnectCount = 0
        while 1:
            try:
                reconnectCount = reconnectCount + 1
                if(reconnectCount > 1):
                    print("Try reconnect count " + str(reconnectCount))
                self.client.connect((ip, port))       #要连接的IP与端口
                print(self.client)
                reconnectCount = 0
                self._socket_thread_read = 1

                threadRead = ThreadRun("read", self.threadReadRun)
                threadRead.setDaemon(True)  # 子线程随主线程退出
                threadRead.start()
                
                threadInput = ThreadRun("input", self.threadInputRun)
                threadInput.setDaemon(True)
                threadInput.start()
                

                print("Connect ok! ==============================")
                break
            except Exception as e:
                print("Connected error！" + str(e)) 
                time.sleep(self.threadReturnDeta)

     


    # 读取一条消息
    def readImpl(self):
        data = self.client.recv(self._head_size)
        res = ""                 #读取结果缓冲区
        if(data):
            # 读取包头
            # struct中:!代表Network order，3I代表3个unsigned int数据
            headPack = struct.unpack('!1I', data[:self._head_size])
            bodySize = headPack[0]      #数据包长度
            # print("recv head", data, bodySize)

            lastReadLen = bodySize   #剩余需要读取的长度
            while(lastReadLen > 0):
                if(lastReadLen > self.maxReadLen):
                    readLength = self.maxReadLen
                    lastReadLen = lastReadLen - self.maxReadLen
                else:
                    readLength = lastReadLen
                    lastReadLen = 0

                data = self.client.recv(readLength)
                # print("recv body", data)
                res = res + data
            res = res
        return res
    # 发送一条消息       
    def sendImpl(self, jsonstr):
        length = len(jsonstr)
        # byte4 = struct.pack('<i', length)   # 转换 int 4byte 低位前置
        # bytejson = bytes(jsonstr)
        # struct.unpack('<i', p)      # 逆转 4byte int 
        print("send>>>>>>>>>>>>>>>")
        print(jsonstr)
     
        header = [length]
        # struct中:!代表Network order，3I代表3个unsigned int数据
        headPack = struct.pack("!1I", *header)
        data = headPack+jsonstr.encode('utf-8')
        self.client.send(data)

    # 当收到一条消息
    def onReceive(self, jsonstr):
        print("recv<<<<<<<<<<<<<<<<")
        print(jsonstr) 
        fromMsg = yaml.safe_load(jsonstr)
        # print(fromMsg)

        msgType = fromMsg["msgType"]
        if(msgType == 0):
            if(fromMsg["ok"] == "true"):
                print("认证成功！")
                print("SysKey: " + fromMsg["fromSysKey"] + "  key: " + fromMsg["fromKey"])
            else:
                print("重新认证")
                self.loginOn()
        elif(msgType == 1):
            print("发送结果:" + fromMsg["ok"])
        elif(msgType == 10):
            # print(fromMsg)
            msg = ServiceServer().do(fromMsg)
            msg = fromMsg
            self.sendImpl(msg.toString())
        else:
            print("不理解的消息类型")
            print(fromMsg)


    def loginOn(self):
        msg = Msg()
        msg.msgType = 0
        msg.toKey = "qwer"
        msg.fromKey = "f"
        msg.fromSysKey = "fs"
        self.sendImpl(msg.toString())


















if __name__ == '__main__':
    serverSocket = ServerSocket()

    # main = start("192.168.1.6", 8092)
    main = serverSocket.start("39.107.26.100", 8092)
    while 1:
        pass





