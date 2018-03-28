#!/usr/bin/env python
#-*- coding:utf-8 -*- 
import os
import json
import re
import codecs
import sys
#import chardet
import time

try:
    import RPi.GPIO as GPIO    
except RuntimeError:
    print("Error importint RPI.GPIO!") 


#plan the ports to user
s_gpios = [ 11, 12, 13, 15, 16, 18, 22, 7 ]
s_gpioshigh = [ 29, 31, 33, 35, 37, 32, 36, 38, 40 ]
s_gnds = [ 6, 9, 14, 20, 25, 30, 34, 39 ] 
s_gin = []
s_gout = []
s_gnd = []

#init the system gpios
System.init()

class System:
"""  提供系统端口集中控制   """
    
    @staticmethod   # 属于类的一种方法，但无法访问类或实例的属性
    def init(self):
        # BOARD编号方式，基于插座引脚编号    
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)  
        GPIO.setup(s_gpios, GPIO.OUT, initial=0)
        #输入配置 
        GPIO.setup(s_gpioshigh, GPIO.IN) 
        s_gin = System.inputPort(s_gpioshigh)
        s_gout = System.makePort(s_gpios)
        s_gnd = System.makePort(s_gnds)

    @staticmethod
    def getGin():
        return s_gin
    @staticmethod
    def getGout():
        return s_gout
    @staticmethod
    def getGnd():
        return s_gnd


# 同步async 异步sync
# 完全控制
# port, hz, dcFrom, dcTo, dcDeta, sleepTime
    @staticmethod
    def controlPwmAsync(port, hz, dcFrom, dcTo, dcDeta, sleepTime):
        timeStart = int(time.time()*1000)

        # 12 15 deta:2 -> 12,14,16/15
        dcNow = dcFrom
        while (dcNow <= dcTo):

            do something

            time.sleep(sleepTime)

            if(dcNow >= dcTo):
                break
            dcNow = dcNow + dcDeta
            if(dcNow > dcTo):
                dcNow = dcTo

        timeStop = int(time.time()*1000)
        timeDeta = timeStop - timeStart

        return timeDeta



    

    def openPortPwm(port, hz, dc):
        
        return
    @staticmethod
    def setPortPwm(port, hz, dc):
        
        return
    @staticmethod
    def closePortPwm(port):
        
        return




    @staticmethod
    def setPort(port, value):
        for i in range(len(s_gout)): 
            if(s_gout[i]["port"] == port):
                s_gout[i]["value"] = value
                GPIO.output(port, value)

    @staticmethod
    def openPort(port):
        for i in range(len(s_gout)): 
            if(s_gout[i]["port"] == port):
                s_gout[i]["value"] = 1
                GPIO.output(port, 1)

        
    @staticmethod
    def closePort(port):
        for i in range(len(s_gout)): 
            if(s_gout[i]["port"] == port):
                s_gout[i]["value"] = 0
                GPIO.output(port, 0)

    
    @staticmethod
    def inputPort(arr): 
        res = range(0, len(arr))
        i = 0
        for port in arr: 
            status = GPIO.input(port)  
            res[i] = { "port" : port, "value" : status }
            i += 1 
        return res

    @staticmethod
    def makepPort(arr):
        res = range(0, len(arr))
        i = 0
        for port in arr:  
            res[i] = { "port" : port, "value" : 0 }
            i += 1   
        return res
    



