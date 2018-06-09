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
import thread
import subprocess as sp
import numpy as np
import socket
import struct
import yaml
import random   # int(random.uniform(1, 10))
import uuid

import cv2


##############################
# 导入父目录为可引用路径
sys.path.append("../")
sys.path.append("../opencv/")

##########################
# 导入单例装饰器函数 : @singleton
from python_singleton import singleton
# 导入工具 模块 .py : tool.exe()
import tool
import C
from cvhelp import CvHelp
import MSGTYPE



def sleep(mills):
    tool.sleep(mills)
# 日志
def out(*objs):
    print(objs)
    return
# 耗时
def timeMark():
    return int(time.time()*1000)
def timeOut(timeStart, info=''):
    timeStop = int(time.time()*1000)
    timeDeta = timeStop - timeStart
    out(info + ' cost ' + str(timeDeta))

# 线程操作类
class ThreadRun (threading.Thread):
    def __init__(self, name, runCallback, daemon=True):
        threading.Thread.__init__(self)
        self.name = name
        self.runCallback = runCallback
        self.setDaemon(daemon)  # 子线程随主线程退出

    def run(self):
        print "============Thread Start " + self.name
        self.runCallback()
        print "==Thread Stop  " + self.name

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








from python_sqlite import Database

# 数据库工具
from ServiceDb import ServiceDb 

# 导入普通类
from template import Template
from cv_makecolor import MakeColor

# 导入模块Class
from system import System
from ModelTurn import ModelTurn
from ModelMove import ModelMove
from ModelOn import ModelOn
from ModelHcSro4 import ModelHcSro4
from ModelDht11 import ModelDht11

# 导入服务
from Msg import Msg

from ServiceServer import ServiceServer

from server_socket import ServerSocket
# from server_http import ServerHttp


from ServerCamera import ServerCamera
from ServerSensor import ServerSensor











