#!/usr/bin/python
#-*- coding:utf-8 -*-

import re
import sys
import time
import json
import traceback

import tool
import BeautifulSoup
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
        print(self.__module__ + "." + self.name + "." + str(obj))
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

        return

    # 认证登录
    def login(self):
        self.out("尝试登录:")
        # {CONF_VARS: "*", ORG_VARS: true, logintype: "mobile", id: "18408249138", password: "1234qwer"}
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
        self.out(obj)
        # "USER_TOKEN": "caf2ea9cec1f283c8588340a3583d756",
        self.token = obj.get("USER_TOKEN", "")






        pass
        return







if __name__ == '__main__':
    obj = AutoCochat("Test")
    obj.test()