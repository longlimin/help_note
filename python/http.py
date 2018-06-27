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
            "User-Agent":"Mozilla/6.0",
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
        response = "error" 
        try:
            response = self.opener.open(url)
            # self.show(response)
        except Exception as e:
            print(e)
        return response
    def doPost(self, url, postData):
        response = "error" 
        try:
            if(postData):
                postData = urllib.urlencode(postData)
                response = self.opener.open(url, postData) 
                # response = urllib2.urlopen(urllib2.Request(url, data, header))
            else:
                response  = self.opener.open(url)
            # self.show(response)
        except Exception as e:
            print(e)

        return response

 