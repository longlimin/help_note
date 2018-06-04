#!/usr/bin/env python
#-*- coding:utf-8 -*-   
 
from include import *
########################################
from server_socket import ServerSocket
from server_http import ServerHttp

from ServiceCamera import ServiceCamera


############################
# 启动后台s

# Socket后台
serverSocket = ServerSocket()
serverSocket.start("39.107.26.100", 8092)

# ServiceHttp 处理http请求
serverHttp = ServerHttp()
serverHttp.start(8086)

# 线程 Opencv监控摄像头 识别图像 调用socket推送消息
serviceCamera = ServiceCamera(serverSocket)
serviceCamera.start()

# 线程 各种传感器监控 轮循监控


while 1:
    pass






