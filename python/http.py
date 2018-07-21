#!/usr/bin/python
#-*- coding:utf-8 -*-  
import urllib
import urllib2
import cookielib
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
            tool.line()
            self.out(str(url))
            self.out(traceback.format_exc())
        return response
    def doPost(self, url=None, postData=None):
        response = "error" 
        try:
            if(postData != None):
                postData = urllib.urlencode(postData)
                response = self.opener.open(url, postData) 
            else:
                response  = self.opener.open(url)
            # self.show(response)
        except Exception as e:
            tool.line()
            self.out(str(url))
            self.out(str(postData))
            self.out(traceback.format_exc())
        return response
    def do(self, url=None, postData=None):
        if(url != None and url != ""):
            return self.doPost(url, postData)
        return "error, url=null?"
    def doJson(self, url="", postData=None):
        res = {}
        responce = self.do(url, postData)
        if(type(responce) == str):
            jsonStr = responce
        else:
            jsonStr = responce.read()
        if(jsonStr != None and type(jsonStr) == str):
            jsonStr = jsonStr.strip()
            res = tool.toJson(jsonStr)
        else:
            self.out("responce 读取失败,url:" + str(url) + " data:" + str(postData))
        return res















