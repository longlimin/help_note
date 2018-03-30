#!/usr/bin/env python
#-*- coding:utf-8 -*-  

import json
import os
import sys

########################################
# from cv_makecolor import MakeColor
# 不需要上下文的工具类
############################
# 使用方式
# import tool
# tool.exe



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














        