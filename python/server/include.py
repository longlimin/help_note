#!/usr/bin/env python
#-*- coding:utf-8 -*-  

#############################
# 导入常用工具模块
import sys
import os
import json
import re
import codecs
import time
import threading


##############################
# 导入父目录为可引用路径
sys.path.append("../")
sys.path.append("../opencv/")

##########################
# 导入单例装饰器函数 : @singleton
from python_singleton import singleton

# 导入工具 模块 .py : tool.exe()
import tool


# 导入测试 模块
import testModel

# 导入普通类
from template import Template




# 线程读取socket
class ThreadRun (threading.Thread):
    def __init__(self, name, runCallback):
        threading.Thread.__init__(self)
        self.name = name
        self.runCallback = runCallback

    def run(self):
        print "Thread Start " + self.name
        self.runCallback()
        print "Thread Stop  " + self.name

def json_load_byteified(file_handle):
    return _byteify(
        json.load(file_handle, object_hook=_byteify),
        ignore_dicts=True
    )

def json_loads_byteified(json_text):
    return _byteify(
        json.loads(json_text, object_hook=_byteify),
        ignore_dicts=True
    )

def _byteify(data, ignore_dicts = False):
    # if this is a unicode string, return its string representation
    if isinstance(data, unicode):
        return data.encode('utf-8')
    # if this is a list of values, return list of byteified values
    if isinstance(data, list):
        return [ _byteify(item, ignore_dicts=True) for item in data ]
    # if this is a dictionary, return dictionary of byteified keys and values
    # but only if we haven't already byteified it
    if isinstance(data, dict) and not ignore_dicts:
        return {
            _byteify(key, ignore_dicts=True): _byteify(value, ignore_dicts=True)
            for key, value in data.iteritems()
        }
    # if it's anything else, return it in its original form
    return data