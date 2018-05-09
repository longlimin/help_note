#!/usr/bin/env python
#-*- coding:utf-8 -*-   
 
from include import *
########################################
from server_socket import ServerSocket

 

############################
# 启动后台

# 线程 Socket后台
serverSocket = ServerSocket()
main = serverSocket.start("39.107.26.100", 8092)

# ServiceServer 处理普通消息


# 线程 Opencv监控摄像头 识别图像 调用socket推送消息




while 1:
    pass






