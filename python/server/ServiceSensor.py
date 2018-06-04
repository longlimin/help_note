#!/usr/bin/env python
#-*- coding:utf-8 -*- 
from include import *
# from ModelTurn import ModelTurn
# from ModelMove import ModelMove
from ModelMq2 import ModelMq2
from ModelHcSro4 import ModelHcSro4
from ModelDht11 import ModelDht11

@singleton
class ServiceSensor:
    """ 
        Service 
        轮循监控传感器状态
    """ 
    def __init__(self, serverSocket):
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


# 开启轮循
    def start(self):
        nowt = 0
        min = 0.1
        de = 1 / min
        while(True):

            if(nowt % (1 * de / 5) == 0):             # 0.2s
                pass
                ModelOn().get(self.callbackOn)      #通用状态
            elif(nowt % (1 * de) == 0):             # 1S
                pass
            elif(nowt % (2 * de) == 0):           # 2S
                ModelHcSro4().get(self.callbackHcSro4)  # 超声波
                pass
            elif(nowt % (5 * de) == 0):           # 5S
                pass
            elif(nowt % (10 * de) == 0):           # 10S
                pass
            elif(nowt % (150 * de) == 0):           # 120S
                pass
                ModelDht11().get(self.callbackDht11)    # 温湿度


            nowt += 1
            nowt = nowt % 6000
            sleep(min)

        return

    def callbackOn(self, res=[0, 1, 0, 0]):
        pass
        
    def callbackDht11(self, res=(0, 0)):
        pass
    def callbackHcSro4(self, res=0):
        pass




if __name__ == '__main__':
    serviceSensor = ServiceSensor(False)

    serviceSensor.start()
