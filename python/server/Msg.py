#!/usr/bin/env python
#-*- coding:utf-8 -*- 
from include import *

# @singleton
class Msg:
    """Socket send server msg struct""" 
    msgType = 0
    toSysKey = ""
    toKey = ""
    fromSysKey = ""
    fromKey = ""
    info = ""
    ok = ""
    data = {}

    def __init__(self):
        self.info = "from terminal"

        self.msgType = -1                #默认广播本系统
        self.toSysKey = "raspberrypi"   #默认发给本系统 
        # msg.toKey = "1000"
        
  
    def toString(self):
        res = {
            "msgType":self.msgType,
            "toSysKey":self.toSysKey,
            "toKey":self.toKey,
            "fromSysKey":self.fromSysKey,
            "fromKey":self.fromKey,
            "info":self.info,
            "ok":self.ok,
            "data":self.data,
        }
        return json.dumps(res)

        