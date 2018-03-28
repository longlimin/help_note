#!/usr/bin/env python
#-*- coding:utf-8 -*- 

import tornado.ioloop
import tornado.web

########################################
from system import System

############################

#/do/system/home/aaa
class HandlerSystem(tornado.web.RequestHandler): 
    def post(self, method, params):
        self.get(method, params)
        return
    def get(self, method, params):
        params = params.encode('utf-8')
        method = method.encode('utf-8')
        print("class:  " + self.__class__.__name__)    #className
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

    def setports(self, params):    
        port = params.split("-")[0]
        value = params.split("-")[1] 
        print(port, value)
        if(value == "0"):
            System.closeport(int(port))
        else:
            System.openport(int(port))
            
        self.getports(params)
        return

    def getports(self, params): 
        res = {
            "gin" : System.getGin(),
            "gout" : System.getGout(),
            "gnd" : System.getGnd(), 
        }
        print(res)
        
        self.write(res)
        return

    def home(self, params) : 
        print("exec home")
        #print(params)   
        uptime = Tools.exe("uptime")
#top - 14:15:23 up 5 days, 51 min,  3 users,  load average: 0.01, 0.01, 0.00
#Tasks: 139 total,   1 running, 138 sleeping,   0 stopped,   0 zombie
#%Cpu(s):  0.2 us,  0.2 sy,  0.0 ni, 99.6 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st 
#KiB Mem :   949580 total,   400472 free,    50768 used,   498340 buff/cache
#KiB Swap:   102396 total,   102396 free,        0 used.   833200 avail Mem       
        mem = Tools.exe("top -n 1 | grep 'KiB Mem' ") 
        print(mem)
        #print(chardet.detect(mem) )  
  
        
       #mem = re.split(r'.*: +|, +| ',mem)     
        swap = Tools.exe("top -n 1 | grep 'KiB Swap' ")
        
        obj = {
            "uptime": uptime,
            "mem": mem,
            "swap": swap, 
        }
        
        res = json.dumps(obj)
        print(res)
        self.write(res)
        return
        
        
        
        
        
        
        
        

        
        
        




 