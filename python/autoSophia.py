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
        self.roomIndex = {} #房间号 及其<用户>信息
        self.roomMsg = {}   #消息 记录
        self.roomId = ""  #当前房号

        self.robot = Robot()
        self.http = Http()
        self.name = "CC"
        self.count = int(name[6:999])
        self.lastMsgTime = int(time.time() * 10000 ) * 1.0 / 10000  #上一次更新房间聊天记录时间
        self.lastEchoTime = tool.getNowTime()   #上次说话时间
        self.maxDetaTime = 1000 * 60 * 3   # 最大沉默时间
        self.lastMusicTime = tool.getNowTime() 
        self.maxMusicTime = 1000 * 60 * 4
        self.count = -1
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

    def help(self):
        print(dir(self))
    def showUser(self, user, show=True):
        userInfo ="U " + tool.fill(user.get("device", ""), ' ', 15) +  " " + tool.fill(user.get("icon", ""), ' ', 15) + " "  + user.get("name", "")
        if(show):
            self.out(userInfo)
        return userInfo
    def showRoom(self, roomId, show=True, i=0):
        room = self.roomIndex.get(roomId, "")
        if(room == ""):
            self.getRooms()
        room = self.roomIndex.get(roomId, "")
        info = ""
        if(room != ""):
            info = ("##" + tool.fill(str(i), '#', 40) + "\n--G " + tool.fill(room["id"], ' ', 15) + " " + tool.fill(str(room["total"]) + "/" + str(room["limit"]), ' ', 15) + " " + room["name"]) + "\n" 
            # info = info + "开启音乐: " + str(room.get("music", "")) + " 静态房间: " + str(room.get("staticRoom", "")) + ""  
            # info = info + " 隐藏房间: " + str(room.get("staticRoom", "")) + " 游戏房间: " + str(room.get("gameRoom", "")) + " 成人房间: " + str(room.get("adultRoom", "")) + "\n" 
            info = info + "Host: \n--" + self.showUser(room.get("host", {}), False) + "\n" 
            info = info + "Users: " + "\n"
            for item in room.get("users", []):
                info = info + "--" + self.showUser(item, False) + "\n"
        if(show):
            self.out(info)
        return info
    def showAllRoom(self):
        if(self.roomIndex is None or self.roomIndex == "" or self.roomIndex == {}):
            self.getRooms()
        tool.line()
        self.out("展示所有房间信息")
        i = 0
        for key in self.roomIndex:
            # room = self.roomIndex[key]
            self.showRoom(key, True, i)
            i = i+1
        tool.line()

    def showUserRoom(self, userName="小氷", userId="8f1b61e25098b0427f01d724716b70cb"):
        i=0
        for key in self.roomIndex:
            room = self.roomIndex[key]
            users = room.get("users", [])
            for user in users:
                if(user.get("name", "") == userName or user.get("id", "") == userId):
                    self.showRoom(key, True, i)
            # self.showRoom(key, True, i)
            i = i+1


    def goRoom(self, roomId):
        # tool.line()
        self.out("加入房间:" + roomId)
        self.showRoom(roomId)
        responce=self.http.doGet("http://drrr.com/room/?id=" + roomId)
        self.roomId = roomId
        self.send("/me 大家好 我是" + self.name)
        return
    def outRoom(self):
        self.out("离开房间:" + self.roomId)
        self.send("/me CC好无聊啊 要出去溜达一会儿 ")
        self.send("/me 我一定会回来的! ")
        self.showRoom(self.roomId)
        responce=self.http.doPost("http://drrr.com/room/?ajax=1", {
                        "leave":"leave", 
                })
        self.roomId = ""
        return 
    def getRooms(self, detail=False):
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
        while(True):
            if(self.roomId != ""):
                self.out("开启定时发言，最大发言间隔" + str(self.maxDetaTime / 1000) + "s")
            while(self.roomId != ""):
                try:
                    # message = "Now Time is "+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    detaTime = tool.getNowTime() - self.lastEchoTime # ms
                    if(detaTime > self.maxDetaTime):
                        message = "/me 不知道该说什么(⊙﹏⊙)"
                        self.send(message)
                        self.out(str(i) + "\t" + message)
                    detaTime = tool.getNowTime() - self.lastMusicTime # ms
                    if(detaTime > self.maxMusicTime):
                        (url, name, count) = self.robot.getMusic(self.count)
                        self.count = count
                        self.music(url, name)

                    time.sleep(10)
                except Exception as e:
                    print(e)
            # self.out("当前房间roomId:" + self.roomId + " 未加入房间 暂时停止sayHello ")
            time.sleep(3)
    # 定时抓取消息
    def getHello(self):
        tt = 1
        while(True):
            if(self.roomId != ""):
                self.out("开启抓取发言，" + str(tt) + "s/次")
            while(self.roomId != ""):
                try:
                    obj = self.rece()
                    if(obj != ""):
                        self.makeHello(obj)
                    time.sleep(tt)
                except Exception as e:
                    print(e)

            # self.out("当前房间roomId:" + self.roomId + " 未加入房间 暂时停止getHello ")
            time.sleep(3)
    # 抓取发言    json Obj
    def rece(self):
        # 获取最新时间的消息1530004210 157 s秒
        res = ""
        responce=self.http.doGet("http://drrr.com/json.php?fast=1&update="+str(self.lastMsgTime))
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
        self.out("Send." + message)
        responce=self.http.doPost("http://drrr.com/room/?ajax=1", {
                        "message":message, # [0:self.count * 4],
                        "url":"",
                })
        # self.out("发送[" + message + "]" + re[0:66])
        self.lastEchoTime = tool.getNowTime()
        return
    # 分享音乐
    def music(self, url, name="Unknow"):
        if(url == ""):
            return
        self.out("Music." + url + " " + name )
        responce=self.http.doPost("http://drrr.com/room/?ajax=1", {
                        "name":name,
                        "url":url,
                })
        self.lastMusicTime = tool.getNowTime()
        return


    # 手动控制
    def inputHello(self):
        self.out("开启输入监控！")
        self.help()
        while(True):
            try:
                cmd=raw_input("")
                if(cmd != ""):
                    cc = cmd.split(' ')
                    method = cc[0]
                    ret = hasattr(self, method) #因为有func方法所以返回True 
                    if(ret == True) :
                        method = getattr(self, method)#获取的是个对象
                        if(callable(method)):
                            if(len(cc) >= 2):
                                method(cc[1]) 
                            else:
                                method()
                        else:
                            print(method)
                    else:
                        self.out("手动发送:" + cmd)
                        self.send(cmd)
                        time.sleep(1)
            except Exception as e:
                print(e)
        return
    # 抓取到消息的auto回复
    def makeHello(self, obj):
        res = ""
        try:
            # tool.line()
            # print("抓取到消息obj")
            # print(obj)
            self.lastMsgTime = obj.get("update", self.lastMsgTime)
            talks = obj.get('talks', "")
            users = obj.get('users', "")
            if(users != ""):
                room = self.roomIndex.get(self.roomId, "")
                if(room != ""):
                    self.roomIndex[self.roomId]['users'] = users
                else:
                    self.roomIndex[self.roomId] = obj
            # tool.line()
            # print("talks:")
            # print(talks)
            # print("users:")
            # print(users)
            # tool.line()
            if(talks != ""):
                for item in talks:
                    # print(item)
                    msgId = item.get('id', " ")
                    msgType = item.get('type', 'message')
                    msgData = ""
                    msgFromName = item.get('from', {}).get('name', "")
                    if(msgFromName == ""):
                        msgFromName = item.get('user', {}).get('name', "")
                    if(msgType == 'me'):
                        msgData = item.get('content', "")
                    elif(msgType == 'message'):
                        msgData = item.get('message', "")
                    elif(msgType == 'join'):
                        # msgFromName = item.get('user', {}).get('name', "")
                        msgData = '欢迎' + msgFromName + ' の !'
                    elif(msgType == 'leave'):
                        msgData = ' ' + msgFromName + ' 默默的离开了 の... '
                    elif(msgType == 'music'):
                        msgData = item.get('name', "")

                    # print(msgId, msgType, msgData, msgFromName)
                    if( self.roomMsg.get(msgId, "") != "" or msgFromName == self.name or msgFromName == "" ): #已经处理过 或者是自己发送的 或者取出发送者失败
                        pass
                    else:  #未处理过 
                        detaTime = tool.getNowTime() - self.lastEchoTime # ms 60s
                        ran = tool.getRandom(0,self.maxDetaTime) / 1000 - 5    #0-180
                        weight = (self.maxDetaTime - detaTime) / 1000
                        self.out("发言权" + tool.fill(str(weight) + "" , ' ', 8) + " 随机数" + tool.fill(str(ran),' ', 8) + " fromName:" + tool.fill(msgFromName,' ',12) + " msgType:"+tool.fill(msgType,' ',10) + " " + msgData)

                        flag = 0 #不回复
                        if(msgType == 'message' or msgType == 'me' ):    #普通聊天消息
                            if( re.search('@' + self.name + " ", msgData) != None ):    #有@自己
                                msgData = msgData[len(self.name) + 2: 9999]
                                flag = 1
                            elif(ran > weight and  re.search('@', msgData) == None): # 没有@ 且 权重高
                                flag = 1
                        else: #事件 
                            flag = 2

                        res = ""
                        if(flag == 1):  
                            robotRes = self.robot.do(msgData, self.name)
                            code = str(robotRes.get("code", ""))
                            if(code[0:1] != '4'):
                                res = '@' + str(msgFromName) +" " + robotRes.get("text", "")
                            else:
                                self.out("robot接口调用失败 code=" + code)
                        elif(flag == 2):
                            res = msgData

                        if(res != "" and flag != 0):
                            res = '/me ' + res
                            self.send(res)
                        
                    self.roomMsg[msgId] = item #标记未已经处理 历史消息
        except Exception as e:
            print("Exception:" + str(e))
        # tool.line()
        return res
    
    

    def test(self):
        self.login()
        self.getRooms()
        self.goRoom("c74BSkQUra") 
        ThreadRun( "SayHello." + str(self.count),  self.sayHello ).start()
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