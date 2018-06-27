#!/usr/bin/python
#-*- coding:utf-8 -*-  
import tool
from http import Http
import time
import json

class Robot:
    """机器人智能语义应答""" 

    id = ""
    name = ""

    def __init__(self):
        self.id = "test id"
        self.name = "test name"
        self.http = Http()
        self.apiKey = "bfbf6432b655493b9e861b470bca9921"
        self.userId = "WalkerDust"

    def set(self, id, name):
        self.id = id
        self.name = name

        return self

    def toString(self):
        res = ""
        res = self.id + " - " + self.name

        return res  

    def do(self, msg):
        res = "" 
        print("robot send:" + str(msg))
        response = self.http.doPost('http://www.tuling123.com/openapi/api', {
                "key":self.apiKey,
                "info":msg,
                # "userInfo":{
                #     "apiKey":self.apiKey,
                #     "userId":self.userId,
                # },
                # "reqType":0,
                # "perception":{
                #     "inputText":{
                #         "text":msg,
                #     }
                # },
            }
        )
        jsonStr = response.read()

        if(jsonStr != ""):
            res = tool.makeObj(json.loads(jsonStr))
            code = res.get("code", "")
            if(code == 100000):
                 print("robot访问成功 " + jsonStr)
        return res
    def test(self):
        while(True):
            cmd=raw_input("")
            if(cmd != ""):
                res = self.do(cmd)
                print(res)
                time.sleep(1)

        return





if __name__ == '__main__':
    r = Robot()
    r.test()
        