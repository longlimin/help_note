#!/usr/bin/env python
#-*- coding:utf-8 -*- 

import tornado.ioloop
import tornado.web
import os
import json
import re
import commands
import codecs
import sys
#import chardet
import time

try:
    import RPi.GPIO as GPIO    
except RuntimeError:
    print("Error importint RPI.GPIO!") 
# BOARD编号方式，基于插座引脚编号    
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)  
gpios = [ 11, 12, 13, 15, 16, 18, 22, 7 ]
gpioshigh = [ 29, 31, 33, 35, 37, 32, 36, 38, 40 ]
gnds = [ 6, 9, 14, 20, 25, 30, 34, 39 ] 
gin = []
gout = []
gnd = []
GPIO.setup(gpios, GPIO.OUT, initial=0)
#输入配置 
GPIO.setup(gpioshigh, GPIO.IN) 
def openport(port):
    for i in range(len(gout)): 
        if(gout[i]["port"] == port):
            gout[i]["value"] = 1
            GPIO.output(port, 1)

    
    
def closeport(port):
    for i in range(len(gout)): 
        if(gout[i]["port"] == port):
            gout[i]["value"] = 0
            GPIO.output(port, 0)

    
    
def inputport(arr): 
    res = range(0, len(arr))
    i = 0
    for port in arr: 
        status = GPIO.input(port)  
        res[i] = { "port" : port, "value" : status }
        i += 1 
    return res
def makeport(arr):
    res = range(0, len(arr))
    i = 0
    for port in arr:  
        res[i] = { "port" : port, "value" : 0 }
        i += 1   
    return res
    
gin = inputport(gpioshigh)
gout = makeport(gpios)
gnd = makeport(gnds)


#/do/system/home/aaa
class SystemHandler(tornado.web.RequestHandler): 
    def get(self, method, params):
        params = params.encode('utf-8')
        method = method.encode('utf-8')
        #self.write("system handler get !method:" + method + " params:" + params)
        print("method: " + method)    #list
        print("params: " + params)    #{arg1: 'a1', arg2: 'a2' }
        #检查成员
        ret = hasattr(self, method) #因为有func方法所以返回True 
        if(ret == True) :
            #获取成员
            method = getattr(self, method)#获取的是个对象
            method(params) 
        else :
            print("该方法不存在")
        
        return
    def uptime(self, params):
        shell = os.popen('top')
        res = shell.read()
        self.write(res)
        return


        
    def setports(self, params):    
        port = params.split("-")[0]
        value = params.split("-")[1] 
        print(port, value)
        if(value == "0"):
            closeport(int(port))
        else:
            openport(int(port))
            
        self.getports(params)
        return
    def getports(self, params): 
        res = {
            "gin" : gin,
            "gout" : gout,
            "gnd" : gnd, 
        }
        print(res)
        
        self.write(res)
        return
    def home(self, params) : 
        print("exec home")
        #print(params)   
        os.system("echo 'exec in python ' ")          
        uptime = os.popen('uptime').read()
#top - 14:15:23 up 5 days, 51 min,  3 users,  load average: 0.01, 0.01, 0.00
#Tasks: 139 total,   1 running, 138 sleeping,   0 stopped,   0 zombie
#%Cpu(s):  0.2 us,  0.2 sy,  0.0 ni, 99.6 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st 
#KiB Mem :   949580 total,   400472 free,    50768 used,   498340 buff/cache
#KiB Swap:   102396 total,   102396 free,        0 used.   833200 avail Mem       
        mem = exe("top -n 1 | grep 'KiB Mem' ") 
        print(mem)
        #print(chardet.detect(mem) )  
  
        
       #mem = re.split(r'.*: +|, +| ',mem)     
        swap = exe("top -n 1 | grep 'KiB Swap' ")
        
        obj = {
            "uptime": uptime,
            "mem": mem,
            "swap": swap, 
        }
        
        res = json.dumps(obj)
        print(res)
        self.write(res)
        return
        
        
        
        
        
        
        
        

        
        
        
    def post(self, method, params):
        self.get(method, params)
        return




def exe(str) : 
#    (status, output) = commands.getstatusoutput(str)
#    return output
    return os.popen(str).read().encode('utf-8') 





    
 