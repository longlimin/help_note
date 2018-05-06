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
_socket_thread_read = 1
client = {}
_head_size = 4
maxReadLen = 1024        #一次性读取最大长度
threadReadDeta = 0.05    #无数据时读取间隔s
threadReturnDeta = 1    #异常恢复间隔s


# 线程读取socket
class ThreadRun (threading.Thread):
    def __init__(self, name, runCallback):
        threading.Thread.__init__(self)
        self.name = name
        self.runCallback = runCallback

    def run(self):
        print "Thread Start " + self.name
        self.runCallback()
        print "Thread Stop  " + self.name

# 监听消息
def threadReadRun():
    global client

    while(1):
        print("threadReadRun start")
        while (_socket_thread_read):
            jsonstr = readImpl(client)
            if(jsonstr):
                onReceive(client, jsonstr)
            time.sleep(threadReadDeta)
        print("threadReadRun stop")
        time.sleep(threadReturnDeta)
# 实现控制台输入推送消息
def threadInputRun():
    global client

    threadInputCount = 0
    while(True):
        print("threadInputRun start" + str(threadInputCount))

        # 能发送前先 认证系统
        loginOn(client)

        while (_socket_thread_read):
            cmd=raw_input("Input words to broadcast:")
            msg = Msg()
            msg.msgType = -2        #广播所有 测试用
            msg.data = {"broadcast":cmd}
            # print("make", jsonstr)
            sendImpl(client, msg.toString())
            time.sleep(threadReadDeta)
        print("threadInputRun stop" + str(threadInputCount))
        threadInputCount = threadInputCount + 1
        time.sleep(threadReturnDeta)


# 链接服务器中转站
def start(ip, port):
    print("Start client socket")
    global client
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)      #定义socket类型，网络通信，TCP
    
    reconnectCount = 0
    while 1:
        try:
            reconnectCount = reconnectCount + 1
            if(reconnectCount > 1):
                print("Try reconnect count " + str(reconnectCount))
            client.connect((ip, port))       #要连接的IP与端口
            print(client)
            reconnectCount = 0
            _socket_thread_read = 1

            threadRead = ThreadRun("read", threadReadRun)
            threadRead.setDaemon(True)  # 子线程随主线程退出
            threadRead.start()
            
            threadInput = ThreadRun("input", threadInputRun)
            threadInput.setDaemon(True)
            threadInput.start()
            

            print("Connect ok! ==============================")
            break
        except Exception as e:
            print("Connected error！" + str(e)) 
            time.sleep(threadReturnDeta)

 


# 读取一条消息
def readImpl(client):
    data = client.recv(_head_size)
    res = ""                 #读取结果缓冲区
    if(data):
        # 读取包头
        # struct中:!代表Network order，3I代表3个unsigned int数据
        headPack = struct.unpack('!1I', data[:_head_size])
        bodySize = headPack[0]      #数据包长度
        # print("recv head", data, bodySize)

        lastReadLen = bodySize   #剩余需要读取的长度
        while(lastReadLen > 0):
            if(lastReadLen > maxReadLen):
                readLength = maxReadLen
                lastReadLen = lastReadLen - maxReadLen
            else:
                readLength = lastReadLen
                lastReadLen = 0

            data = client.recv(readLength)
            # print("recv body", data)
            res = res + data
        res = res
    return res
# 发送一条消息       
def sendImpl(client, jsonstr):
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
    client.send(data)

# 当收到一条消息
def onReceive(client, jsonstr):
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
            loginOn(client)
    elif(msgType == 1):
        print("发送结果:" + fromMsg["ok"])
    elif(msgType == 10):
        # print(fromMsg)
        msg = ServiceServer().do(fromMsg)
        sendImpl(client, msg.toString())
    else:
        print("不理解的消息类型")
        print(fromMsg)


def loginOn(client):
    msg = Msg()
    msg.msgType = 0
    msg.toKey = "qwer"
    msg.fromKey = "f"
    msg.fromSysKey = "fs"
    sendImpl(client, msg.toString())


















if __name__ == '__main__':
    # main = start("192.168.1.6", 8092)
    main = start("39.107.26.100", 8092)
    while 1:
        pass





