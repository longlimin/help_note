#!/usr/bin/env python
#-*- coding:utf-8 -*-  
from include import *
import threading
import json
import thread
import socket
import struct
########################################
from ServiceMsg import ServiceMsg

############################
_socket_thread_read = 1
client = {}

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

 
def threadReadRun():
    global client

    while(1):
        print("threadReadRun start")
        while (_socket_thread_read):
            jsonstr = readImpl(client)
            onReceive(client, jsonstr)
            time.sleep(1)
        print("threadReadRun stop")
        time.sleep(1)
def threadInputRun():
    global client

    threadInputCount = 0
    while(1):
        print("threadInputRun start" + str(threadInputCount))
        while (_socket_thread_read):
            cmd=raw_input("Please input cmd:")
            sendImpl(client, cmd)
            time.sleep(0.1)
        print("threadInputRun stop" + str(threadInputCount))
        threadInputCount = threadInputCount + 1
        time.sleep(3)



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
            time.sleep(1)

 


# 读取一条消息
def readImpl(client):

    return "test"
# 发送一条消息       
def sendImpl(client, jsonstr):
    length = len(jsonstr)
    byte4 = struct.pack('<i', length)   # 转换 int 4byte 低位前置
    bytejson = bytes(jsonstr)
    byte = byte4 + bytejson
    # struct.unpack('<i', p)      # 逆转 4byte int 
    print("send:" + byte)
    client.sendall(byte)
# 当收到一条消息
def onReceive(client, jsonstr):
    # print("onReceive:" + str(jsonstr))
    # onReceive(client.recv(2))
    pass
if __name__ == '__main__':
    main = start("127.0.0.1", 8091)
    while 1:
        pass





