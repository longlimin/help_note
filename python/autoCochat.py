#!/usr/bin/python
#-*- coding:utf-8 -*-

import re
import sys
import time
import json
import traceback
import uuid
import tool
import BeautifulSoup
from socketIO_client import SocketIO
from socketIo import Socket

from http import Http
from tool import ThreadRun
from python_sqlite import Database



# cochat 自动化
class AutoCochat:
    def __init__(self, name="Test"):
        self.name = name

        self.http = Http()
        self.db = Database()
        self.db.execute(
            ''' 
            create table if not exists music(
                url         text primary key,
                name        text,
                fromName    text,
                count       text
            )
            ''' )

        return
    # 日志输出
    def out(self, obj):
        print(time.strftime("%Y%m%d %H:%M:%S", time.localtime()) + "." + self.name + "." + str(obj))
        return
    # 实时控制帮助
    def help(self):
        self.out(dir(self))
        return
    # doMethod([methodName arg1 arg2]) -> methodName(arg1,arg2)
    def doMethod(self, listArgs):
        size = len(listArgs)
        res = None
        if(size > 0):
            if(hasattr(self, listArgs[0])):
                method = getattr(self, listArgs[0])
                if(callable(method)):
                    if(size == 2):
                        res = method(listArgs[1])
                    elif(size == 3):
                        res = method(listArgs[1], listArgs[2])
                    elif(size == 4):
                        res = method(listArgs[1], listArgs[2], listArgs[3])
                    elif(size == 5):
                        res = method(listArgs[1], listArgs[2], listArgs[3], listArgs[4])
                    else:
                        res = method()
                else:
                    self.out(method)
        return res
    # 手动命令监控
    def inputHello(self):
        self.out("开启输入监控！")
        self.help()
        while(True):
            try:
                cmd=raw_input("")
                if(cmd != ""):
                    if(not self.doMethod(cmd.split(" "))):
                        self.doCmd(cmd)
                        time.sleep(1)
            except Exception as e:
                self.out(repr(e))
        return
    # 测试用
    def test(self):
        self.login()
        ThreadRun( "InputHello." + str(self.name),  self.inputHello ).start()
        tool.wait()
        return
    # 监控执行
    def doCmd(self, cmd):
        self.send({"data":cmd})
        return

    # 认证登录
    def login(self):
        self.out("尝试登录:")
        # {CONF_V   ARS: "*", ORG_VARS: true, logintype: "mobile", id: "18408249138", password: "1234qwer"}
# Request URL:http://picc.cochat.cn/SY_ORG_LOGIN.login.do?DESKTOP_OS=Win10&USER_LAST_BROWSER=Win32&USER_LAST_CLIENT=2.5.1&USER_LAST_OS=DESKTOP&USER_LAST_PCNAME=%7B%7D
#
# Set-Cookie:user_token=278d168a95af8661d6eddbdfe6dba59e; path=/
# Set-Cookie:login_name=18408249138; path=/
# request Cookie:JSESSIONID=abcb0skaQYCGs6lvy9orw
        obj = self.http.doJson("http://picc.cochat.cn/SY_ORG_LOGIN.login.do?DESKTOP_OS=Win10&USER_LAST_BROWSER=Win32&USER_LAST_CLIENT=2.5.1&USER_LAST_OS=DESKTOP&USER_LAST_PCNAME=%7B%7D",{
            "CONF_VARS":"*",
            "ORG_VARS":"true",
            "logintype":"mobile",
            "id":"18408249138",
            "password":"1234qwer"
        })
        self.loginUser = obj
        self.out("登录结果:")
        # self.out(obj)
        # "USER_TOKEN": "caf2ea9cec1f283c8588340a3583d756",

        token = obj.get("USER_TOKEN", "")
        urlWithPort = obj.get("CONF_VARS", {}).get("@C_SY_COMM_SOCKET_SERV_V1.0@", "http://cochat.cn:9091")
        if(urlWithPort.find("http://") < 0):
            urlWithPort = "http://" + urlWithPort
        # http://cochat.cn:9091
        uus = urlWithPort.split(':')
        port = int(uus[2])
        # url = "ws:" + uus[1] + ":" + uus[2]
        url = uus[1][2:999] #cochat.cn 不需要ws http 只需要ip 域名
        # ws://127.0.0.1:9002"
        # 182.92.224.228
        # hosts = 'ws:\/\/cochat.cn'

        self.socketServerUrl = urlWithPort
        self.socketUrl = url
        self.socketPort = port
        self.showUser()



        self.config = {
            "transports":['websocket', 'polling'],  # websocket优先
            "timeout":5 * 1000, # 超时时间
            "forceNew": True,
            "reconnection" : False
        };
        self.out("socket开始")
        # self.socket = SocketIO(url,port=port) # , params=self.config)
        self.socket = Socket(url, port)
        self.out("socket连接完成，开始初始化事件")

        socketMsgTypes = ("connect", "disconnect","error","connect_error","connect_timeout","connecting","reconnecting","message", "event")
        # for item in socketMsgTypes:
        #     if(hasattr(self, item)):
        #         method = getattr(self, item)
        #         if(callable(method)):
        #             self.socket.on(item, method)
        #         else:
        #             self.out("变量而非方法" + item + "回调?")
        #     else:
        #         self.out("属性" + item + "不存在，是否写错了名字?")
        self.socket.on("message", self.message)

        self.out("socket初始化事件完成，开始发送认证")
        self.data = {
            "userName":obj.get("USER_CODE", ""),
            "displayName": "ccc",# tool.encode(obj.get("ORG_VARS", {}).get("@USER_NAME@", "") ),
            "odept":obj.get("ORG_VARS", {}).get("@ODEPT_CODE@", ""),
            "token":obj.get("USER_TOKEN", ""),
            "uuid":str(uuid.uuid1()),
            "version":obj.get("USER_CODE", "") + "_LAST_MSG"
        }
        self.out(self.data)
        self.socket.emit('loginv17', self.data, self.onSocketLogin)
        self.out("已发送认证信息")
        return
    def connect(self, *args):
        print("connect", args)
        self.socket.emit('loginv17', self.data, self.onSocketLogin)
        return
    def disconnect(self, *args):
        print("disconnect", args)
        return
    def error(self, *args):
        print("error", args)
        return
    def connect_error(self, *args):
        print("connect_error", args)
        return
    def connect_timeout(self, *args):
        print("connect_timeout", args)
        return
    def connecting(self, *args):
        print("connecting", args)
        return
    def reconnect(self, *args):
        print("reconnect", args)
        return
    def reconnecting(self, *args):
        print("reconnecting", args)
        return
    def message(self, *args):
        print("message", args)
        return
    def event(self, *args):
        print("event", args)
        return
    def onSocketLogin(self, *data):
        self.out("socket登录回调:")
        print(data)
        return

    def send(self, type, data):
        self.socket.send(type, data)
        return


    def showUser(self):
        tool.line()
        obj = self.loginUser
        user = obj.get("ORG_VARS", {})
        self.out(user.get("@USER_NAME@", ""))
        self.out(user.get("@USER_POST@", ""))
        self.out(user.get("@LOGIN_NAME@", ""))
        self.out("USER_CODE:" + obj.get("USER_CODE", ""))
        self.out("USER_TOKEN:" + user.get("UESR_TOKEN", ""))
        self.out("socketServerUrl:" + self.socketServerUrl)
        self.out("to url:" + self.socketUrl)
        self.out("to port:" + str(self.socketPort))

        tool.line()
        return
if __name__ == '__main__':
    obj = AutoCochat("Test")
    obj.test()