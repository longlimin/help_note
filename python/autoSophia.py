#!/usr/bin/python
#-*- coding:utf-8 -*-  
 
import json
import time
import BeautifulSoup
import tool
from http import Http
from tool import ThreadRun
from robot import Robot
import re

class AutoSophia:
    def __init__(self, name="00000"):
        self.roomIndex = {}
        self.roomMsg = {}

        self.robot = Robot()
        self.http = Http()
        self.name = "CCC"
        self.count = int(name[6:999])
        self.lastMsgTime = int(time.time() * 10000 ) * 1.0 / 10000
        self.lastEchoTime = tool.getNowTime()   #上次说话时间
        self.maxDetaTime = 1000 * 60 * 3   #min
    def out(self, obj):
        print(self.name + "." + obj)
    def login(self):
        # tool.line()
        self.out("访问主页 获取 token session")
        responce = self.http.doGet('http://drrr.com/')
        re = responce.read()
        soup =BeautifulSoup.BeautifulSoup(re)
        # self.out soup.prettify()
        nameList = soup.findAll('input',{'name':{'token'}})
        if(len(nameList) > 0):
            token = nameList[0]['data-value']
            token = tool.encode(token)
            self.out("抓取成功: ")
            self.out("token\t " + token)
            self.out("cookie\t " + tool.toString(self.http.getCookie()))

            # tool.line()
            self.out("模拟登录")
            responce=self.http.doPost('http://drrr.com/', {
                        "name":self.name,
                        "login":"ENTER",
                        "token":token,
                        "direct-join":"",
                        "language":"zh-CN",
                        "icon":"zaika-2x",
                })
        else:
            self.out("error！ 没能抓取到token")

    def goRoom(self, roomId):
        # tool.line()
        self.out("加入房间:" + roomId)
        room = self.roomIndex.get(roomId, "")
        if(room != ""):
            self.out("#" + "\t" + room["id"] + " " + str(room["total"]) + "/" + str(room["limit"]) + "\t " + room["name"])

        responce=self.http.doGet("http://drrr.com/room/?id=" + roomId)
        return
    def getRooms(self):
        tool.line()
        self.out("房间列表")
        responce=self.http.doGet("http://drrr.com/lounge?api=json")
        jsonObj = tool.makeObj(json.loads(responce.read()))
        rooms = jsonObj["rooms"]
        for i in range(len(rooms)):
            room = rooms[i]
            self.roomIndex[room["id"]] = room
            self.out("#" + str(i) + "\t" + room["id"] + " " + str(room["total"]) + "/" + str(room["limit"]) + "\t " + room["name"])
        self.out("解析完毕")
    # 定时发送消息
    def sayHello(self):
        # tool.line()

        while(True):
            message = "Now Time is "+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            # self.send(message)
            self.out(str(i) + "\t" + message)
            time.sleep(200)
    # 定时抓取消息
    def getHello(self):
        tt = 5
        self.out("开始抓取发言，" + str(tt) + "s/次")
        while(True):
            obj = self.rece()
            if(obj != ""):
                self.makeHello(obj)
            time.sleep(tt)

    # 抓取发言    json Obj
    def rece(self):
        # 获取最新时间的消息1530004210 157 s秒
        res = ""
        nowTime = self.lastMsgTime
        self.out("抓取发言 t=" + str(nowTime) )
        responce=self.http.doGet("http://drrr.com/json.php?update="+str(nowTime))
        if(responce != ""):
            jsonStr = responce.read()
            if(jsonStr != ""):
                res = tool.makeObj(json.loads(jsonStr))
            else:
                res = ""
        return res
    # 发送消息
    def send(self, message):
        if(message == ""):
            return
        responce=self.http.doPost("http://drrr.com/room/?ajax=1", {
                        "message":message, # [0:self.count * 4],
                        "url":"",
                })
        return
    # 手动输入发送消息
    def inputHello(self):
        while(True):
            cmd=raw_input("")
            if(cmd != ""):
                self.out("手动发送:" + cmd)
                self.send(cmd)
                time.sleep(1)

        return
    # 抓取到消息的auto回复
    def makeHello(self, obj):
        res = ""
        try:
            tool.line()
            print("抓取到消息")
            print(obj)
            self.lastMsgTime = obj.get("update", self.lastMsgTime)
            talks = obj.get('talks', "")
            if(talks != ""):
                for item in talks:
                    msgId = item['id']
                    msgType = item['type']
                    msgData = ""
                    if(msgType == 'me'):
                        msgData = item['content']
                    else:
                        msgData = item['message']

                    msgFromName = item['from']['name']
                    his = self.roomMsg.get(msgId, "")
                    if(his != "" or msgFromName == self.name ): #已经处理过 或者是自己发送的
                        pass
                    else:  #未处理过
                        detaTime = tool.getNowTime() - self.lastEchoTime # ms
                        ran = tool.getRandom(0,self.maxDetaTime)
                        self.out("发言间隔 = " + str(detaTime / 1000) + "s" + " 随机数 = " + str(ran / 1000))
                        if(re.search('@' + self.name, msgData) != None or ran > self.maxDetaTime - detaTime):  # @自己才回复
                            robotRes = self.robot.do(msgData)
                            if(robotRes != ""):
                                code = str(robotRes.get("code", ""))
                                if(code[0:1] != '4'):
                                    res = robotRes.get("text", "")
                                    res = '/me @' + str(msgFromName) + ' ' + res
                                    self.send(res)
                                    self.roomMsg[msgId] = msgData
                                    self.lastEchoTime = tool.getNowTime()
                                else:
                                    self.out("robot接口调用失败 code=" + code)
                        pass
        except Exception as e:
            print(e)
        return res
    def test(self):
        self.login()
        self.getRooms()
        self.goRoom("siSpBMbllV") # roomIndex.keys()[0])
        self.send("大家好 我是" + self.name)
        # ThreadRun( "SayHello." + str(self.count),  self.sayHello ).start()
        ThreadRun( "GetHello." + str(self.count),  self.getHello ).start()
        ThreadRun( "InputHello." + str(self.count),  self.inputHello ).start()

        tool.wait()
        return
if __name__ == '__main__':
    size = 1
    objs = []
    for i in range(size):
        obj = AutoSophia("Walker" + str(i))
        objs.append(obj)
    for i in range(size):
        ThreadRun( "Robot." + str(i), objs[i].test ).start()
        time.sleep(10)
    tool.wait()