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
        self.name = "CD"
        self.count = int(name[6:999])
        self.lastMsgTime = int(time.time() * 10000 ) * 1.0 / 10000  #上一次更新房间聊天记录时间
        self.lastEchoTime = tool.getNowTime()   #上次说话时间
        self.maxDetaTime = 1000 * 60 * 3   # 最大沉默时间
        self.lastMusicTime = tool.getNowTime() 
        self.maxMusicTime = 1000 * 60 * 5
        self.musicNow = {}
        self.musicPlayType = -1
        self.ifOnMusic = False
        self.tail = " の... "
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
        self.send("/me 大家好 我是暖手宝" + self.name + " 可以@我 点歌name(*^_^*) 通常只是沉默潜水 不会打扰大家啦 @必回哟(大概) Ps.不@也可能会回O(∩_∩)O")
        return
    def outRoom(self):
        self.out("离开房间:" + self.roomId)
        self.send("/me " + self.name + "好无聊啊 "+self.name +"要出去溜达一会儿" + self.tail)
        self.send("/me "+self.name+"一定会回来的" + self.tail)
        self.showRoom(self.roomId)
        responce=self.http.doPost("http://drrr.com/room/?ajax=1", {
                        "leave":"leave", 
                })
        self.roomId = ""
        return 
    def getRooms(self, detail=False):
        tool.line()
        # self.out("房间列表")
        responce=self.http.doGet("http://drrr.com/lounge?api=json")
        jsonObj = tool.makeObj(json.loads(responce.read()))
        rooms = jsonObj["rooms"]
        for i in range(len(rooms)):
            room = rooms[i]
            self.roomIndex[room["id"]] = room
            # self.out("#" + str(i) + "\t" + room["id"] + " " + str(room["total"]) + "/" + str(room["limit"]) + "\t " + room["name"])
        # self.out("解析完毕")
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
                        message = "/me ^ ^"
                        self.send(message)
                        self.out(str(i) + "\t" + message)
                    detaTime = tool.getNowTime() - self.lastMusicTime # ms
                    if(self.ifOnMusic and detaTime > self.maxMusicTime):
                        self.playMusic()

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
                        "message":message, # [0:self.musicPlayType * 4],
                        "url":"",
                })
        # self.out("发送[" + message + "]" + re[0:66])
        self.lastEchoTime = tool.getNowTime()
        return
    # 分享音乐
    def playMusic(self, url="", name="", fromName=""):
        if(url[0:4] != "http"):
            music = self.robot.getMusic(name, fromName, self.musicPlayType)
            # self.musicPlayType = count
            url = music.get("url", "")
            name = music.get("name", "")
            fromName = music.get("fromName", "")
            if(fromName != ""):
                self.send("/me 一首" + name + "送给" + fromName + "" + self.tail)
        if(url == ""):
            return
        self.out("url=" + url + " name=" + name + " fromName=" + fromName )
        responce=self.http.doPost("http://drrr.com/room/?ajax=1", {
                        "music":"music",
                        "name":name,
                        "url":url,
                })
        self.musicNow = {"url":url, "name":name, "fromName":fromName}
        self.lastMusicTime = tool.getNowTime()
        return
    def listMusic(self):
        print(self.robot.listMusic)
    # 切歌控制 on/off/turn/prev/next/remove
    def music(self, cmd="on"):
        self.out("music:" + cmd)
        if(cmd == "on"):
            self.ifOnMusic = True
            self.send("/me 已经打开音乐点播" + self.tail)
        elif(cmd == "off"):
            self.ifOnMusic = False
            self.send("/me 已经关闭音乐点播" + self.tail)
        elif(cmd == "turn"):
            self.ifOnMusic = True
            self.musicPlayType = 0
            self.playMusic()
        elif(cmd == "prev"):
            self.ifOnMusic = True
            self.musicPlayType = -1
            self.playMusic()
        elif(cmd == "next"):
            self.ifOnMusic = True
            self.musicPlayType = 1
            self.playMusic()
        elif(cmd == "remove"):
            self.robot.removeMusic(self.musicNow.get("url", ""))
            self.send("/me 降低音乐" + self.musicNow.get("name") + "播放频率 " + self.tail)

        return 
    # 手动控制
    def inputHello(self):
        self.out("开启输入监控！")
        self.help()
        while(True):
            try:
                cmd=raw_input("")
                if(cmd != ""):
                    if(not self.doMethod(cmd.split(" "))):
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
            if(talks != ""):
                for item in talks:
                    # print(item)
                    msgId = item.get('id', " ")
                    msgType = item.get('type', 'message')
                    msgData = ""
                    msgFromName = item.get('from', {}).get('name', "")
                    if(msgFromName == ""):
                        msgFromName = item.get('user', {}).get('name', "")

                    if( self.roomMsg.get(msgId, "") != "" or msgFromName == self.name or msgFromName == "" ): #已经处理过 或者是自己发送的 或者取出发送者失败
                        break



                    if(msgType == 'me'):
                        msgData = item.get('content', "")
                    elif(msgType == 'message'):
                        msgData = item.get('message', "")
                    elif(msgType == 'join'):
                        # msgFromName = item.get('user', {}).get('name', "")
                        msgData = '欢迎' + msgFromName + self.tail
                    elif(msgType == 'leave'):
                        msgData = ' ' + msgFromName + ' 默默的离开了 ' + self.tail
                    elif(msgType == 'music'):
                        music = item.get('music', {})
                        name = music.get('name', '')
                        url = music.get('url', '')
                        music = { "name":name, "url":url, "fromName":msgFromName }
                        self.robot.addMusic(music) #添加用户分享记录
                        self.musicNow = music
                        self.lastMusicTime = tool.getNowTime()
                        msgData = self.name + '悄悄的的把' + msgFromName + '喜欢的歌' + name + '给记在小本子上 '  + self.tail

                    self.roomMsg[msgId] = item #标记未已经处理 历史消息

                    detaTime = tool.getNowTime() - self.lastEchoTime # ms 60s
                    ran = tool.getRandom(0,self.maxDetaTime) / 1000 - 5    #0-180
                    weight = (self.maxDetaTime - detaTime) / 1000
                    self.out("发言权" + tool.fill(str(weight) + "" , ' ', 6) + " 随机数" + tool.fill(str(ran),' ', 6) + " fromName:" + tool.fill(msgFromName,' ',12) + " msgType:"+tool.fill(msgType,' ',10) + " " + msgData)

                    flag = 0 #不回复
                    if(msgType == 'message' or msgType == 'me' ):    #普通聊天消息
                        if( re.search('@' + self.name + " ", msgData) != None):    #有@自己 且权重不太低
                            ran = tool.getRandom(0,100)
                            if(ran > 6):
                                msgData = msgData[len(self.name) + 2: 9999]
                                flag = 1
                            else:
                                self.out("@权重=" + str(ran) + "太小！！！！！！！！！！！！！！")
                                flag = 2
                                msgData = "突然不想说话"+self.tail
                        elif(ran > weight and  re.search('@', msgData) == None): # 没有@ 且 权重高
                            flag = 1
                    else: #事件 
                        flag = 2

                    res = ""
                    if(flag == 1):
                        if(self.filterCmd(msgData, msgFromName)):    #若过滤器未处理 则继续交由下面处理
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
                        
        except Exception as e:
            print("Exception:" + str(e))
        # tool.line()
        return res
    # /do help   指令控制行为 
    def filterCmd(self, msgData="", fromName=""):
        res = True
        msgData = msgData.strip()

        # name 点歌
        # 点歌 name
        # 点 name 这首歌
        flag = False
        ppp = ['点歌','music','歌曲','点播','下面播放', '想听']
        ooo = [
            ('一首','献给大家'),
            ('一首','送给大家'),
            ('点','这首歌'),
        ]
        size = len(msgData)
        # print(flag, msgData)
        for item in ppp:
            itemLen = len(item)
            index = msgData.find(item)
            if(index == 0): #头命中
                msgData = msgData[itemLen:9999].strip()
                flag = True
                break
            elif(index == size - itemLen):# 尾命中
                msgData = msgData[0:size-itemLen].strip()
                flag = True
                break
        if(not flag):
            for before,after in ooo:
                index = msgData.find(before)
                if(index == 0):
                    index1 = msgData.find(after)
                    if(index1+len(after) == size):
                        flag = True
                        # print(len(before), index1)
                        msgData = msgData[len(before):index1].strip()
                        break
        # print(flag, msgData)
        if(flag):#抽离点歌 名字
            res = False
            # fromName, msgData
            self.playMusic(url="", name=msgData, fromName=fromName)
        elif( re.search('/do ', msgData) != None ): 
            res = False
            cmd = msgData[4:9999]
            cmd = cmd.strip()
            cmds = cmd.split(' ')
            # self.out("操控：" )
            # print(cmd, cmds)
            if(len(cmds) > 0 and cmds[0] == ""):
                cmds.pop(0)

            if(not self.doMethod(cmds)):
                self.send("/me ########## @" + self.name + " /do music <on/off/turn/prev/next> ########")

        return res
    # [methodName arg1 arg2]
    def doMethod(self, listArgs):
        size = len(listArgs)
        res = False
        if(size > 0):
            if(hasattr(self, listArgs[0])):
                method = getattr(self, listArgs[0])#获取的是个对象
                if(callable(method)):
                    if(size == 2):
                        method(listArgs[1]) 
                    elif(size == 3):
                        method(listArgs[1], listArgs[2])  
                    elif(size == 4):
                        method(listArgs[1], listArgs[2], listArgs[3]) 
                    elif(size == 5):
                        method(listArgs[1], listArgs[2], listArgs[3], listArgs[4]) 
                    else:
                        method()
                    res = True
                else:
                    print(method)
        return res
 

    def test(self):
        self.login()
        self.getRooms()
        # self.goRoom("c74BSkQUra") 
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
    time.sleep(99999)