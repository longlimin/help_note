#!/usr/bin/env python
#-*- coding:utf-8 -*-  

import json
import os
import sys
import time
import uuid
import random
########################################
# from cv_makecolor import MakeColor
# 不需要上下文的工具类
############################
# 使用方式
# import tool
# tool.exe

# img二维数组 压缩 value=0-255 100/height
# 1字节Byte = 8bit = 256编码  16进制2位 2f
def makeByte(img):
    res = ''
    size = img.size
    for row in img:
        for col in row:
            res += hex(col)[2:4]
    return res

def getRandom(start=0, stop=10):
    return int(random.uniform(start, stop))

def getUuid():
    return (str(uuid.uuid1())).split("-")[0]
# 编码问题  
def encode(string):
    t = type(string)
    res = string
    if(t == unicode):
        # res = res.encode('unicode-escape').decode('string_escape') 
        res = res.encode('utf-8')
        # print(t, string, "->", res)
    elif(t == int):
        pass
    else:
        pass
    return res

# 获取某个模块或者 class 值为value的变量名
def getClassName(cla, value):
    keys = dir(cla)
    for key in keys:
        ret = hasattr(cla, key) 
        if(ret == True) :
            method = getattr(cla, key)#获取的是个对象
            if(value == method):
                return key

    return "None key"


#exe the shell cmd, return the string encode by utf-8
def exe(str):
    # (status, output) = commands.getstatusoutput(str)
    # return output
    return os.popen(str).read().encode('utf-8') 

# do the method of the class, *params动态参数 元组 也可以作为动态参数传递
def doMethod(cls, methodName, *params):
    print('# do method')
    print("class:  " + cls.__class__.__name__)    #className
    print("method: " + methodName)    #list
    print("params: " + str(params))    #{arg1: 'a1', arg2: 'a2' }
    #检查成员
    ret = hasattr(cls, methodName) #因为有func方法所以返回True 
    if(ret == True) :
        #获取成员
        method = getattr(cls, methodName)#获取的是个对象
        # length = len(params)
        # if(length == 0):
        #     return method()
        # else:
        return method(*params)
    else :
        print("Error! 该方法不存在")
    return ''

def sleep(mills):
    time.sleep(mills)

def getNowTime():
    return int(time.time()*1000)











        