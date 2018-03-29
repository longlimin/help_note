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

















        