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

# 音乐选择
    def getMusic(self, count=-1):
        url = ""
        name = ""
        with open('music.txt', 'r') as f:  
            data = f.readlines()  #txt中所有字符串读入data  
            
            if(count == -1):
                count = tool.getRandom(0, len(data))
            else:
                while(True):
                    temp = tool.getRandom(0, len(data))
                    if(temp != count):
                        count = temp
                        break
            name = data[count]
            url = "http://39.107.26.100:8088/file/" + name

        return (url, name, count)
# 智能应答 
    def do(self, msg, userId="CC"):
        res = "" 
        response = self.http.doPost('http://www.tuling123.com/openapi/api', {
                "key":self.apiKey,
                "info":msg,
                "userid":userId,
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
            print("Robot. " + str(msg) + " -> " + jsonStr)
        else:
            print("Robot. " + str(msg) + " -> error !!!!!!!!! ")
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
    # print(r.getMusic())
    # print(r.getMusic(1))
        