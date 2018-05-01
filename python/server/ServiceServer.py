#!/usr/bin/env python
#-*- coding:utf-8 -*- 
from include import *
from Msg import Msg

from ModelTurn import ModelTurn
from ModelMove import ModelMove

@singleton
class ServiceServer:
    """ 
        Service 
        Return map by map
        Control the system
    """ 

    def do(self, fromMsg):
        data = fromMsg["data"]

        #消息处理 默认发给请求者
        msg = Msg()
        msg.toSysKey = fromMsg["fromSysKey"]
        msg.toKey = fromMsg["fromKey"]
        msg.data = {}
        msg.msgType = 10                #单点回传
        msg.data["res"] = "true"
        msg.data["info"] = "info"
        msg.data["method"] = data.get("method", "no method ? ")

        msg = self.doMethod(msg, msg.data["method"], data.get("params", ""))
        return msg
 


    def doMethod(self, msg, method, params):
        # params = params.encode('utf-8')
        # method = method.encode('utf-8')

        # tool.doMethod(self, method, params)
        print("class:  " + self.__class__.__name__)    #className
        print("method: " + method)    #list
        print("params: " + params)    #{arg1: 'a1', arg2: 'a2' }
        #检查成员
        ret = hasattr(self, method) #因为有func方法所以返回True 
        if(ret == True) :
            #获取成员
            method = getattr(self, method)#获取的是个对象
            return method(msg, params) 
        else :
            print("Error ! 该方法不存在")
            msg.data["res"] = "false"
            msg.data["info"] = "该方法不存在"
            return msg

# left right head back space stop
    def move(self, msg, param):
        print("move", param)
        params = param.split("-")[0]
        if(params == 'left'):
            ModelMove().turnLeft()
        elif(params == 'right'):
            ModelMove().turnRight()
        elif(params == 'head'):
            ModelMove().moveHead()
        elif(params == 'back'):
            ModelMove().moveBack()
        elif(params == 'space'):
            ModelMove().space()
        elif(params == 'stop'):
            ModelMove().stop()
        elif(params == 'faster'):
            ModelMove().moveFaster(1)
        elif(params == 'slower'):
            ModelMove().moveFaster(-1)
        elif(params == 'movefasterto'):
            dc = param.split("-")[1]
            dc = int(dc)
            ModelMove().moveFaster(dc)
        elif(params == 'turnrevert'):
            ModelMove().turnRevert()



        msg.data["info"] = "move"
        return msg

# 0 1 
    def cameraTurn(self, params):
        # obj = json.loads(params)
        ff = int(params)
        if(params == "0"):
            deta = 20
            (ifMove, info, costTime) = ModelTurn().turnDeta(deta)
        elif(params == "1"):
            deta = -20
            (ifMove, info, costTime) = ModelTurn().turnDeta(deta)
        elif(ff == -1):
            deta = 0
            (ifMove, info, costTime) = ModelTurn().turnTo()
        else:
            (ifMove, info, costTime) = ModelTurn().turnTo(ff)

        res = {
            "ifmove":ifMove,
            "info":info,
            "costtime":costTime,
        }
        print(res)
        
        msg.data["res"] = json.dumps(res)
        return msg















 
    def toString(self):
        res = "" 

        return res

        