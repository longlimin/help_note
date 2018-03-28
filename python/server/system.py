#!/usr/bin/env python
#-*- coding:utf-8 -*- 
import os
import json
import re
import codecs
import sys
import time

try:
    import RPi.GPIO as GPIO    
except RuntimeError:
    print("Error importint RPI.GPIO!") 




# 单例装饰器
def singleton(cls):
    instances = {}
 
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
 
    return wrapper

######################################
@singleton
class System: 

    #plan the ports to user
    #           L6  R6  L7  L8  R8  R9  R11 L4     L-6 -5  -4 -3  -2
    s_gpios = [ 11, 12, 13, 15, 16, 18, 22, 7,     29, 31, 33,35, 37 ]
    #                R-5 R-3 -2  -1
    s_gpioshigh = [  32, 36, 38, 40 ]
    #          R3 L5 
    s_gnds = [ 6, 9, 14, 20, 25, 30, 34, 39 ] 
    s_gin = []
    s_gout = []
    s_gnd = []


    def __init__(self):
        print('system.init')
        # BOARD编号方式，基于插座引脚编号    
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)  
        #输出配置
        GPIO.setup(self.s_gpios, GPIO.OUT, initial=0)
        #输入配置 
        GPIO.setup(self.s_gpioshigh, GPIO.IN) 
        self.s_gin = self.inputPort(self.s_gpioshigh)
        self.s_gout = self.makePort(self.s_gpios)
        self.s_gnd = self.makePort(self.s_gnds)

    def getGin(self):
        print(self.s_gin)
        return self.s_gin
    def getGout(self):
        return self.s_gout
    def getGnd(self):
        return self.s_gnd




# 同步async 异步sync
# 
# 完全控制 生成dc区间序列 周期控制渐变 dc
# port, hz, dcFrom, dcTo, dcDeta, sleepTime
    def controlPwmAsync(self, port, hz, dcFrom, dcTo, dcDeta, sleepTime):
        timeStart = int(time.time()*1000)

        # print('from', dcFrom,'to->', dcTo,'deta', dcDeta, sleepTime) 
        
        pwm = GPIO.PWM(port, hz) #通道12 50hz
        pwm.start(0)    #空置

        
        # 12 15 deta:2 -> 12,14,16/15
        dcNow = dcFrom

        if(dcTo > dcFrom):  #递增
            while (dcNow <= dcTo):
                pwm.ChangeDutyCycle(dcNow)    #改变占比

                time.sleep(sleepTime)


                if(dcNow >= dcTo):
                    break
                dcNow = dcNow + dcDeta
                if(dcNow > dcTo):
                    dcNow = dcTo
        elif(dcTo < dcFrom): #递减
            while (dcNow >= dcTo):
                pwm.ChangeDutyCycle(dcNow)    #改变占比

                time.sleep(sleepTime)


                if(dcNow <= dcTo):
                    break
                dcNow = dcNow - dcDeta
                if(dcNow < dcTo):
                    dcNow = dcTo
        pwm.stop()

        timeStop = int(time.time()*1000)
        timeDeta = timeStop - timeStart

        return timeDeta



    

    def testPwm(self, port, hz, dc):
        self.p = GPIO.PWM(port, hz) #通道12 50hz
        self.p.start(0) 
        self.p.ChangeDutyCycle(dc)
        time.sleep(2)

        for d in range(15):
            self.p.ChangeDutyCycle(d)
            time.sleep(0.3)
        # time.sleep(0.005)  
        p.stop()

    def openPortPwm(self, port, hz, dc):
        self.p = GPIO.PWM(port, hz) #通道12 50hz
        self.p.start(dc) 
        # p.ChangeDutyCycle(dc)
        # time.sleep(0.005)  
        # p.stop()
        return
    @staticmethod
    def setPortPwm(self, port, hz, dc):
        self.p.ChangeDutyCycle(dc)
        return
    @staticmethod
    def closePortPwm(self, port):
        self.p.stop()
        return




    def setPort(self, port, value):
        for i in range(len(self.s_gout)): 
            if(self.s_gout[i]["port"] == port):
                self.s_gout[i]["value"] = value
                GPIO.output(port, value)

    def openPort(self, port):
        for i in range(len(self.s_gout)): 
            if(self.s_gout[i]["port"] == port):
                self.s_gout[i]["value"] = 1
                GPIO.output(port, 1)

        
    def closePort(self, port):
        for i in range(len(self.s_gout)): 
            if(self.s_gout[i]["port"] == port):
                self.s_gout[i]["value"] = 0
                GPIO.output(port, 0)

    
    def inputPort(self, arr): 
        res = range(0, len(arr))
        i = 0
        for port in arr: 
            status = GPIO.input(port)  
            res[i] = { "port" : port, "value" : status }
            i += 1 
        return res

    def makePort(self, arr):
        res = range(0, len(arr))
        i = 0
        for port in arr:  
            res[i] = { "port" : port, "value" : 0 }
            i += 1   
        return res
    



 