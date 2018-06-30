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
import traceback

class Http:
    def __init__(self):
        self.cookie = cookielib.CookieJar()
        self.cookieHander = urllib2.HTTPCookieProcessor(self.cookie)
        self.opener = urllib2.build_opener(self.cookieHander)

        header = {
            "User-Agent":"Mozilla/6.0",
        }
        turnHeader = []
        for item in header.keys():
            turnHeader.append( (item, header[item]) )
            
        self.opener.addheaders = turnHeader
        # urllib2.install_opener(opener)  
        return
    def out(self, *obj):
        print("http." + str(obj))
    def getCookie(self):
        res = {}
        for item in self.cookie:
            res[item.name] = item.value
        return res
    def show(self, response):
        tool.line()
        try:
            self.out("Cookie:")
            for item in self.cookie:
                self.out( '##' + item.name + ':' + item.value)

            self.out("Code: " + str(response.getcode()))
            self.out("Res : " + str(response.msg))
            self.out("Headers : ")
            self.out(response.headers)
        except Exception as e:
            self.out(traceback.format_exc())
        tool.line()
        return
    # 访问地址后 set-cookie自动被设置
    def doGet(self, url):
        response = "error" 
        try:
            response = self.opener.open(url)
            # self.show(response)
        except Exception as e:
            self.out(traceback.format_exc())
        return response
    def doPost(self, url=None, postData=None):
        response = "error" 
        try:
            if(postData != None):
                postData = urllib.urlencode(postData)
                response = self.opener.open(url, postData) 
                # response = urllib2.urlopen(urllib2.Request(url, data, header))
            else:
                response  = self.opener.open(url)
            # self.show(response)
        except Exception as e:
            self.out(traceback.format_exc())

        return response
    def do(self, url=None, postData=None):
        if(url != None and url != ""):
            return self.doPost(url, postData)
        return "error"
    def doJson(self, url="", postData=None):
        res = {}
        responce = self.do(url, postData)
        jsonStr = responce.read()
        if(jsonStr != None and type(jsonStr) == str):
            jsonStr = jsonStr.strip()
            if(jsonStr[0:1] == "{"):
                res = tool.makeObj(json.loads(jsonStr))
            else:
                self.out("解析json失败:" + jsonStr[0:200])
        else:
            self.out("responce 读取失败,url:" + str(url) + " data:" + str(postData))
        return res















