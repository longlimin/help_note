#!/usr/bin/env python
#-*- coding:utf-8 -*- 
from include import *
from Msg import Msg

from ModelTurn import ModelTurn
from ModelMove import ModelMove

@singleton
class ServiceCamera:
    """ 
        Service 
        管理摄像头 识别opencv 判断处理 发送监控提醒socket推送
    """ 
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

    def __init__():
        self.ifRtmpPush = "0"

# 开启摄像头监控识别
    def start():

        pass

# 关闭监控识别
    def stop():
        pass

# 开启推送视频
    def openPush():
        self.ifRtmpPush = "1"
# 关闭推送视频
    def closePush():
        self.ifRtmpPush = "0"




 
    def toString(self):
        res = "" 

        return res

        