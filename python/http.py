#!/usr/bin/python
#-*- coding:utf-8 -*-  
import urllib
import urllib2
import cookielib
import sys
import os
import json
import re
import codecs
import time
import threading
import thread
import subprocess
import struct
import yaml
import random   # int(random.uniform(1, 10))
import uuid
import base64
import httplib
import tool
 
class Http:    
    def __init__(self):
        self.cookie = cookielib.CookieJar()
        self.cookieHander = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.cookieHander)

        header = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
        }
        turnHeader = []
        for item in header.keys():
            turnHeader.append( (item, header[item]) )
            
        self.opener.addheaders = turnHeader
        # urllib2.install_opener(opener)  
        return
    def getCookie(self):
        res = {}
        for item in self.cookie:
            res[item.name] = item.value
        return res
    def show(self, response):
        tool.line()
        try:
            print("Cookie:")
            for item in self.cookie:
                print '##' + item.name + ':' + item.value

            print("Code: " + str(response.getcode()))
            print("Res : " + str(response.msg))
            print("Headers : ")
            print(response.headers)
        except Exception as e:
            print(e)
        tool.line()
        return
    # 访问地址后 set-cookie自动被设置
    def doGet(self, url):
        response = self.opener.open(url)
        # self.show(response)
        return response
    def doPost(self, url, postData):
        response = ""
        try:
            if(postData):
                postData = urllib.urlencode(postData)
                response = self.opener.open(url, postData) 
                # response = urllib2.urlopen(urllib2.Request(url, data, header))
            else:
                response  = self.opener.open(url)
            # self.show(response)
        except urllib2.HTTPError as e:
            print(e.code)
            response = "访问异常：" + str(e.code)

        return response



    # print("访问主页 获取 token session")
    # line()
    # r=urllib2.urlopen('http://drrr.com/')
    # show(r)
    # for item in cookie:
    #     print '## ' + item.name + ':' + item.value

    # print("模拟登录")
    # line()
    # r=urllib2.urlopen('http://drrr.com/', urllib.urlencode({
    #             "name":"Walker"+str(tool.getNowTime()),
    #             "login":"ENTER",
    #             "token":"e65e05d0c3c8f3331b9b4540b1e7bd91",
    #             "direct-join":"",
    #             "language":"zh-CN",
    #             "icon":"zaika",
    #     }))
    # show(r)
    # for item in cookie:
    #     print '## ' + item.name + ' ' + item.value

    # line()
    # print("房间列表")
    # r=urllib2.urlopen("http://drrr.com/lounge?api=json")
    # re = r.read()
    # jsonObj = tool.makeObj(json.loads(re))
    # rooms = jsonObj["rooms"]
    # for i in range(len(rooms)):
    #     room = rooms[i]
    #     print("#" + str(i) + "\t" + room["id"] + " " + str(room["total"]) + "/" + str(room["limit"]) + "\t " + room["name"])
    # print("解析完毕")

    # line()
    # print("加入房间")
    # r=urllib2.urlopen("http://drrr.com/room/?id=MvUiHAxNlL")
    # show(r)


    # line()
    # print("开始说话")
    # for i in range(100):
    #     message = "现在的时间是："+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #     print(str(i) + "\t" + message)
    #     r=urllib2.urlopen("http://drrr.com/room/?ajax=1", urllib.urlencode({
    #                 "message":message,
    #                 "url":"",
    #         }))
    #     show(r)
    #     print(r.read())
    #     time.sleep(60)



    # 获取最新时间的消息1530004210 157 s秒
    # http://drrr.com/json.php?update=1530003983.5837
    # "talks": [{
    #         "id": "d684400c9a19258ec599ec30c385eafb",
    #         "time": 1530003918.2105,
    #         "type": "message",
    #         "from": {
    #             "name": "Walker009",
    #             "id": "bbe0520e548b793a08bca658cdd8d968",
    #             "icon": "zaika"
    #         },
    #         "message": "\u73b0\u5728\u7684\u65f6\u95f4\u662f\uff1a2018-06-26 17:05:13"
    #     }

    # print("等待")

    # while(True):
    #     pass