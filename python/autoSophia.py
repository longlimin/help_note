#!/usr/bin/python
#-*- coding:utf-8 -*-  
 
import json
import re
import time
import traceback
import BeautifulSoup
import traceback

import tool
from http import Http
from robot import Robot
from tool import ThreadRun


class AutoSophia:
    def __init__(self, name="0000000", count = 0, makeRooms=[]):
        self.robot = Robot()
        self.http = Http()
        self.name = name
        self.count = count   #编号

        self.listMsgQue = []    #消息发送队列
        self.timeDetaMsgSend = 1.1    #最小发送消息间隔s

        self.makeRooms = makeRooms
        self.roomIndex = {} #房间号 及其<用户>信息
        self.roomMsg = {}   #消息 记录
        self.roomId = ""  #当前房号

        self.init()
        self.tail = " の... "
    def init(self):
        ############### 心情模块
        self.statusMin = 5
        self.statusMax = 95
        self.statusDefault = 80
        self.status = 10     #说话欲望值 0-100
        self.statusOnDeta = 15      #开心
        self.statusOffDeta = 15     #难过
        self.statusDownDeta = 40    #闭嘴

        self.getMsgDetaTime = 1     #抓取消息间隔
        self.lastMsgTime = int(time.time() * 10000 ) * 1.0 / 10000  #上一次更新房间聊天记录时间
        self.lastEchoTime = tool.getNowTime()   #上次说话时间
        self.lastOtherSay = tool.getNowTime()   #上次其他人说话时间
        self.lastEchoTimeQuene = tool.getNowTime()

        self.maxDetaOtherSay = 1000 * 60 * 10 #最大没人说话时间 换房
        self.maxDetaTime = 1000 * 60 * 4   # 最大沉默时间
        self.lastMusicTime = tool.getNowTime() #上次放歌时间
        self.maxMusicTime = 1000 * 60 * 4 #音乐间隔 暂不解析音乐文件时长控制
        self.musicNow = {}
        self.musicPlayType = -1
        self.ifOnMusic = False
        self.notWait = False
    def out(self, obj):
        print(time.strftime("%Y%m%d %H:%M:%S", time.localtime()) + "." + self.name + "." + str(obj))
        return
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

    def showHelp(self):

        self.send("/me @" + self.name + " help 1.点歌 歌名-专辑-主唱    2.打开点播/关闭点播  ")

        self.help()
    def nobody(self):
        self.showHelp()
    def help(self):
        self.out(dir(self))
    def showUser(self, user, show=True):
        userInfo ="U " + tool.fill(user.get("device", ""), ' ', 15) +  " " + tool.fill(user.get("icon", ""), ' ', 15) + " "  + user.get("name", "")
        if(show):
            self.out(userInfo)
        return userInfo
    def showRoom(self, roomId="", show=True, i=0):
        if(roomId == ""):
            roomId = self.roomId
        room = self.roomIndex.get(roomId, "")
        if(room == ""):
            self.getRooms()
        room = self.roomIndex.get(roomId, "")
        info = ""
        if(room != ""):
            info = ("##" + tool.fill(str(i), '#', 40) + "\n--G " + tool.fill(room["id"], ' ', 15) + " " + tool.fill(str(room["total"]) + "/" + str(room["limit"]), ' ', 15) + " " + room["name"]) + "\n" 
            info = info + "music: " + str(room.get("music", False)) + " language:" + room.get("language","") +"\n"  # " 静态房间: " + str(room.get("staticRoom", "")) + ""
            # info = info + " hiddenRoom: " + str(room.get("staticRoom", "")) + " 游戏房间: " + str(room.get("gameRoom", "")) + " 成人房间: " + str(room.get("adultRoom", "")) + "\n"
            info = info + "Host:" + room.get("host", {}).get("name", "") + "\n"
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
    # 获取当前房间人员列表
    def getRoomUsers(self, roomId=""):
        room = self.roomIndex.get(roomId, {})
        users = room.get("users", [])
        return users

    # 获取用户所在房间
    def getUserRoom(self, userName="小氷", userId="8f1b61e25098b0427f01d724716b70cb"):
        i=0
        res = []
        for key in self.roomIndex:
            room = self.roomIndex[key]
            users = room.get("users", [])
            for user in users:
                if(user.get("name", "") == userName):
                    # self.showRoom(key, True, i)
                    res.append(room)
                if(user.get("id", "") == userId):
                    self.showRoom(key, True, i)
            i = i+1
        if(len(res) <= 0):
            self.out("用户不在线"+userName)
        if(len(res) >= 2):
            self.out("该用户多次出现？？？？？")
            for item in res:
                self.out(item)
            tool.line()
        return res
    def goRoomName(self, roomName):
        if(self.roomIndex is None or self.roomIndex == "" or self.roomIndex == {}):
            self.getRooms()
        tool.line()
        self.out("查找房间名字加入" + roomName)
        i = 0
        for key in self.roomIndex:
            room = self.roomIndex[key]
            name = room.get("name", "")
            if(re.search(roomName, name) != None):
                self.goRoom(key)
                break;
            i = i+1
        tool.line()

    def goRoom(self, roomId):
        # tool.line()
        self.out("加入房间:" + roomId)
        # self.showRoom(roomId)
        responce=self.http.doGet("http://drrr.com/room/?id=" + roomId)
        self.roomId = roomId
        self.lastOtherSay = tool.getNowTime() #重置处理时间
        self.init()
        # self.send("/me 大家好 我是暖手宝" + self.name + " 可以@ [点歌/turn/prev](*^_^*) @不一定会回 不@也不一定不会回(∩_∩) ")
        return
    def outRoom(self):
        self.out("离开房间:" + self.roomId)
        # self.send("/me " + self.name + "好无聊啊 "+self.name +"要出去溜达一会儿" + self.tail)
        # self.send("/me "+self.name+"一定会回来的" + self.tail)
        # self.send("/me 出去一下，马上回来" + self.tail)
        self.showRoom(self.roomId)
        time.sleep(self.timeDetaMsgSend *  len(self.listMsgQue) + 1)  #等待一会儿消息发送
        responce=self.http.doPost("http://drrr.com/room/?ajax=1", {
                        "leave":"leave", 
                })
        self.roomId = ""
        if(responce == "error"):
            return False
        return True
    def getRooms(self, detail=False):
        tool.line()
        self.out("获取房间列表")
        responce=self.http.doGet("http://drrr.com/lounge?api=json")
        jsonObj = tool.makeObj(json.loads(responce.read()))
        rooms = jsonObj["rooms"]
        makeRooms = []

        if(len(rooms) > 0):
            self.roomIndex.clear()
            i = 0
            count = 0
            userCount = 0
            for room in rooms:
                id = room.get("id","")
                if(room.get("language","") == "zh-CN"):
                    # root.showRoom(id, show=True, i=i)
                    makeRooms.append(room)
                    self.roomIndex[room["id"]] = room
                    count = count + 1
                    userCount = userCount + int(room.get("total", 0))
                    self.out("#" + tool.fill(str(i),' ',4) + "" + room["id"] + " " + str(room["total"]) + "/" + str(room["limit"]) + "\t " + room["name"])
                i = i + 1


            self.out("共计房间" + tool.fill(str(count), ' ', 5) + " 用户" + tool.fill(str(userCount), ' ', 5) )
        self.out("解析完毕")
        return makeRooms

    # 太久没人发言 时 退出 并 进入一个新的 活跃的房间
    def goARoom(self):
        # self.out("#" + str(i) + "\t" + room["id"] + " " + str(room["total"]) + "/" + str(room["limit"]) + "\t " + room["name"])
        lastRoomId = self.roomId
        nowRoom = self.roomIndex.get(self.roomId, {})
        if(nowRoom.get("total", 0) > 1): #当前房间人数 还有其他人
            self.send("/me 好无聊 去其他房间溜达去了 " + self.tail)
        if(self.roomId != ""):
            self.outRoom()

        while(self.roomId == ""):
            self.getRooms()
            self.out("选择最活跃房间")
            i = 0
            maxNum = 0
            maxKey = ""
            for key in self.roomIndex:
                exist = True
                room = self.roomIndex[key]
                total = room.get("total", 0)
                limit = room.get("limit", 0)
                music = room.get("music", False)
                for item in room.get("users", []):
                    if(item.get("name", "") == self.name):
                        tool.line()
                        self.out("异常! 该房间存在同名用户 无法加入 ")
                        self.showRoom(room.get("id", ""))
                        exist = False
                        break

                if(limit > total and music and exist and room.get("id", "") != lastRoomId): #有空位 且允许放歌 且该房间不存在同名 且并不是上次的房间
                    if(maxNum < total):
                        maxNum = total
                        maxKey = key
                i = i+1
            if(maxKey != ""):
                self.out("选中房间:")
                self.showRoom(maxKey)
                tool.line()
                self.goRoom(maxKey)
            else:
                tool.line()
                self.out("异常！！！！！！！！！ 居然无可用房间？")
                time.sleep(2)
        return

    # 定时消息发送队列
    def doHello(self):
        while(True):
            if(self.roomId != ""):
                self.out("开启消息发送队列 deta=" + str(self.timeDetaMsgSend) + "ms")
                # self.listMsgQue = []
            while(self.roomId != ""):
                try:
                    detaTime = tool.getNowTime() - self.lastEchoTime
                    if(detaTime > self.timeDetaMsgSend): # 发送时差大于最小发送间隔
                        if(len(self.listMsgQue) > 0):
                            msg = self.listMsgQue.pop(0)
                            self.doSend(msg)
                    time.sleep(self.timeDetaMsgSend)
                except Exception as e:
                    self.out("消息发送异常 消息队列:")
                    self.out(self.listMsgQue)
                    self.out(traceback.format_exc())
            # self.out("当前房间roomId:" + self.roomId + " 未加入房间 暂时停止sayHello ")
            time.sleep(3)
    # 定时操作
    def sayHello(self):
        while(True):
            if(self.roomId != ""):
                self.out("开启定时发言，最大发言间隔" + str(self.maxDetaTime / 1000) + "s")
            dt = 0
            theI = 0
            self.lastEchoTimeQuene = tool.getNowTime()
            while(self.roomId != ""):
                try:
                    # message = "Now Time is "+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    detaTime = tool.getNowTime() - self.lastEchoTimeQuene # ms
                    if(detaTime > self.maxDetaTime):
                        message = "/me 存活确认." + str(theI) + "." + time.strftime("%Y%m%d %H:%M:%S")
                        self.send(message)
                        self.out(str(theI) + "\t" + message)
                        theI = theI + 1
                    detaTime = tool.getNowTime() - self.lastMusicTime # ms
                    if(self.ifOnMusic and detaTime > self.maxMusicTime and len(self.getRoomUsers(self.roomId)) > 1 ): #音乐开启 且 太久没放歌曲 且当前房间有至少两个人(包括自己robot)
                        self.playMusic()
                    detaTime = tool.getNowTime() - self.lastOtherSay # ms
                    if(detaTime > self.maxDetaOtherSay and self.notWait): #不不停留True
                        self.goARoom() #10分钟没处理过消息 互动 则换房间

                    if(dt % 600 == 0):
                        self.getRooms() #定时5分钟获取房间最新信息

                    time.sleep(10)
                    dt = dt + 10
                    dt = dt % 3600
                except Exception as e:
                    self.out(traceback.format_exc())
            # self.out("当前房间roomId:" + self.roomId + " 未加入房间 暂时停止sayHello ")
            time.sleep(3)
    # 定时抓取消息##########################
    def getHello(self):
        tt = self.getMsgDetaTime
        while(True):
            if(self.roomId != ""):
                self.out("开启抓取发言，" + str(tt) + "s/次")
            while(self.roomId != ""):
                try:
                    obj = self.rece()
                    if(obj != ""):
                        self.makeHello(obj)
                except Exception as e:
                    self.out(traceback.format_exc())
                time.sleep(tt)
            # self.out("当前房间roomId:" + self.roomId + " 未加入房间 暂时停止getHello ")
            time.sleep(3)
    # 抓取发言    json Obj
    def rece(self):
        # 获取最新时间的消息1530004210 157 s秒
        res = ""
        url = "http://drrr.com/json.php?update="+str(self.lastMsgTime)
        # self.out(url)
        responce=self.http.doGet(url)
        if(responce != "" and type(responce) != str ):
            jsonStr = responce.read()
            if(jsonStr != ""):
                res = tool.makeObj(json.loads(jsonStr))
            else:
                res = ""
        else:
            self.out("请求异常:" + str(responce) ) 
        return res

    # 发送消息-添加队列
    def send(self, message):
        if(message != None and message != ""):
            self.listMsgQue.append(message)
            self.lastEchoTimeQuene = tool.getNowTime()
        return
    # 发送消息
    def doSend(self, message):
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

# 用户权限
    def getUserAuth(selfself, name=""):
        res = ""
        return res
    def play(self, name=""):
        self.playMusic("aaa", name)
    def playurl(self, url=""):
        self.playMusic(url)
    # 分享音乐
    def playMusic(self, url="", name="", fromName=""):
        if(self.roomIndex.get(self.roomId, {}).get("music", False) == False):
            self.send("/me 当前房间禁止音乐播放" + self.tail)
            return

        self.musicPlayType = 0 #重置为随机播放

        if(url[0:4] != "http"): #无地址url则是定向点播
            if(name == ""): #无名字 则自动换
                music = self.robot.turnMusic(self.musicPlayType)
            else:
                self.send("/me 正在搜索歌曲[" + name + "]" + self.tail)
                music = self.robot.getMusic(name, fromName)
            url = music.get("url", "")
            name = music.get("name", "")
            fromName = music.get("fromName", "")
        if(fromName != ""):
            msg = ""
            rooms = self.getUserRoom(fromName)
            if(len(rooms) > 0):
                room = rooms[0]
                if(room.get("id","") == self.roomId): #在当前房间
                    msg = "/me 一首[" + name + "]送给" + fromName + "" + self.tail
                else:
                    pass
                    # msg = "/me Share " + room.get("name")[0:4] + "/" + fromName + "'s[" + name + "]" + "" + self.tail
            else:   #不在线
                pass
                # msg = "/me Then play" + fromName + " ordered [" + name + "]" + "" + self.tail
            self.send(msg)
        self.out("分享歌曲url=" + url + " name=" + name + " fromName=" + fromName )
        if(url == ""):
            self.send("/me 怼不起,没有找到类似的歌曲,瑟瑟发抖"+self.tail)
            return
        responce=self.http.doPost("http://drrr.com/room/?ajax=1", {
                        "music":"music",
                        "name":name,
                        "url":url,
                })
        self.musicNow = {"url":url, "name":name, "fromName":fromName}
        self.lastMusicTime = tool.getNowTime()
        return
    def listMusic(self):
        self.out(self.robot.listMusic)
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
            # self.ifOnMusic = True
            self.musicPlayType = 0
            self.playMusic()
        elif(cmd == "prev"):
            # self.ifOnMusic = True
            self.musicPlayType = -1
            self.playMusic()
        elif(cmd == "next"):
            # self.ifOnMusic = True
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
                    if(not self.doMethod(cmd)):
                        self.out("手动发送:" + cmd)
                        self.send(cmd)
                        time.sleep(1)
            except Exception as e:
                self.out(traceback.format_exc())
        return
    # 抓取到消息的auto回复
    def makeHello(self, obj):
        res = ""
        try:
            # tool.line()
            # self.out("抓取到消息obj")
            # self.out(obj)
            newTime = obj.get("update", self.lastMsgTime)
            newTime = int(newTime)
            # print(newTime)
            self.lastMsgTime = newTime
            talks = obj.get('talks', "")
            users = obj.get('users', "")
            if(users != ""):
                room = self.roomIndex.get(self.roomId, "")
                if(room != ""):
                    self.roomIndex[self.roomId]['users'] = users
                else:
                    self.roomIndex[self.roomId] = obj
            if(talks != ""):
                onceDocount = 0
                for item in talks:
                    # self.out(item)
                    msgTime = item.get("time", tool.getNowTime())
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
                        msgData = '欢迎' + msgFromName + self.tail
                    elif(msgType == 'leave'):
                        msgData = '' + msgFromName + '' + self.tail
                        msgData = ''
                    elif(msgType == 'music'):
                        music = item.get('music', {})
                        name = music.get('name', '')
                        url = music.get('url', '')
                        # msgData = '悄悄的的把[' + name + ']给记在小本子上 '  + self.tail
######################################################## 不处理
                    if( self.roomMsg.get(msgId, "") != ""): #已经处理过 或者是自己发送的 或者取出发送者失败
                        # self.out("旧消息 " + msgId + " type:" + msgType + " data:" + msgData)
                        break

                    if(msgType == "me" or msgType == "message"): #只记录聊天消息
                        self.robot.addMsg(msgId, msgFromName, msgData, msgTime)
                    if( msgFromName == self.name or msgFromName == ""):
                        break
#############################################################
                    self.lastOtherSay = tool.getNowTime()   #重置处理时间

                    if(msgType == 'music'):
                        music = { "name":name, "url":url, "fromName":msgFromName }
                        res = self.robot.addMusic(music) #添加用户分享记录
                        if(res == 1):   #更新则不提示
                            msgData = ""
                        self.musicNow = music
                        self.lastMusicTime = tool.getNowTime()

                    self.roomMsg[msgId] = item #标记未已经处理 历史消息

                    if(self.status>self.statusMax):
                        self.status = self.statusMax
                    elif(self.status < self.statusMin):
                        self.status = self.statusMin

                    detaTime = tool.getNowTime() - self.lastEchoTimeQuene # ms 60s
                    olRan = tool.getRandom(0,self.maxDetaTime) / 1000    #0-180 过于久没有发过消息了 权重高则可能自回复
                    weight = (self.maxDetaTime - detaTime) / 1000   #多久没说话了 最大多长时间必须说话
                    ran = int(1.0 * olRan * (1+ 1.0 * (self.status-90) / 100) )

                    self.out("Msg." + msgId[0:4] + "." + tool.fill(str(weight) + "" , ' ', 5) + " " + tool.fill(str(olRan) + "->" + str(ran),' ', 5) + "." + tool.fill(msgFromName,' ',8) + "."+tool.fill(msgType,' ',4) + "." + msgData)

                    flag = 0 #不回复
                    if(msgType == 'message' or msgType == 'me' ):    #普通聊天消息
                        if( re.search('@' + self.name + " ", msgData) != None):    #有@自己 且权重不太低
                            msgData = re.sub('@' + self.name + " ", "", msgData) #摘除@自己
                            flag = 1
                            # else:
                            #     self.out("@me 随机数=" + str(ran) + " 小于 说话欲望=" + str(self.status) + " ")
                            #     flag = 2
                            #     msg = "生气程度:" + str(100-self.status) + "%,不想搭理"+self.tail
                        elif(ran > weight and  re.search('@', msgData) == None): # 没有@ 且 权重高 主动搭话概率
                            flag = 1
                    else: #事件 
                        flag = 2

                    res = ""
                    if(self.filterFlag(msgData, msgFromName)):    #最高级 权限是否黑名单过滤
                        if(flag == 1):
                            if(self.robot.getUser(msgFromName).get("flag", "0") != "0"):
                                self.out("不想搭理" + msgFromName)
                            else:
                                if(self.filterCmd(msgData, msgFromName)):    #若过滤器未处理 则继续交由下面处理
                                    ran = tool.getRandom(0,100)
                                    if(ran < 8): # 20% @ 自动应答不回
                                        self.out("小概率不接入机器回复")
                                        msgData = ""
                                    else:
                                        robotRes = self.robot.do(msgData, self.name)
                                        code = str(robotRes.get("code", ""))
                                        if(code[0:1] != '4'):
                                            text = self.robot.doParse(robotRes)
                                            res = "..." + text # '@' + str(msgFromName) +" " +
                                        else:
                                            self.out("robot接口调用失败 code=" + code)
                        elif(flag == 2):
                            res = msgData

                        if(res != "" and flag != 0 and onceDocount < 6): # 最多一次抓取发送3个
                            res = '/me ' + res
                            onceDocount = onceDocount + 1
                            self.send(res)
                        
        except Exception as e:
            self.out("Exception:" + str(e))
        # tool.line()
        return res
    # /do help   指令控制行为  /do send /me 你们好
    def filterCmd(self, msgData="", fromName=""):
        res = True
        msgData = msgData.strip()
        flag = False
        size = len(msgData)
        self.out("filterCmd." + msgData + "." + fromName)


        pr = ['打开点歌', '播放音乐', '放歌', '开启放歌']
        if(not flag):
            for item in pr:
                if(msgData == item):
                    msgData = ""
                    self.music("on")
                    flag = True
                    break
        pr = ['关闭点歌', '停止放歌','停止音乐', '别放歌', '关闭放歌','关闭音乐', '别放了']
        if(not flag):
            for item in pr:
                if(msgData == item):
                    msgData = ""
                    self.music("off")
                    flag = True
                    break
        pr = ['prev', '上一曲', '上一首', '换回去']
        if(not flag):
            for item in pr:
                if(msgData == item):
                    msgData = ""
                    self.musicPlayType = -1
                    flag = True
                    break
        nnn = ['下一曲','下一首', '切歌', '换','换歌', '不好听', '难听','难听死了', '换换换','换一首', 'next', 'turn']
        if(not flag):
            for item in nnn:
                if(msgData == item):
                    msgData = ""
                    flag = True
                    break
        ppp = ['点歌','music','歌曲','点播','下面播放', '想听', '播放', '放', 'play', 'mp3']
        if(not flag):
            for item in ppp:
                itemLen = len(item)
                index = msgData.find(item)
                if(index == 0): #头命中
                    msgData = msgData[itemLen:9999].strip()
                    flag = True
                    break
                elif(index > 0 and index == size - itemLen):# 尾命中
                    msgData = msgData[0:size-itemLen].strip()
                    flag = True
                    break
        ooo = [
            ('一首','献给大家'),
            ('一首','送给大家'),
            ('点','这首歌'),
        ]
        if(not flag):
            for before,after in ooo:
                index = msgData.find(before)
                if(index == 0):
                    index1 = msgData.find(after)
                    if(index1+len(after) == size):
                        flag = True
                        msgData = msgData[len(before):index1].strip()
                        break
        if(flag):#抽离点歌 名字
            self.out('filterCmd.' + str(flag) + "." + msgData)
            res = False
            self.playMusic(url="", name=msgData, fromName=fromName)
        if( re.search('/do', msgData) != None ):
            res = False
            cmd = msgData[3:9999]
            self.out(" do method." + str(cmd))
            if(not self.doMethod(cmd)):
                self.help()

        pr = ['help', 'info', '帮助', '介绍']
        if(not flag):
            for item in pr:
                if(msgData == item):
                    msgData = ""
                    self.showHelp()
                    res = False
                    break
        pr = ['wait', 'master', 'stay']
        if(not flag):
            for item in pr:
                if(msgData == item):
                    msgData = ""
                    self.notWait = False
                    self.send("/me " + self.name + " 决定在这里住下来" + self.tail)
                    res = False
                    break
        pr = ['go', 'out', 'leave']
        if(not flag):
            for item in pr:
                if(msgData == item):
                    msgData = ""
                    self.notWait = True
                    self.send("/me " + self.name + " 这就离开" + self.tail)
                    self.outRoom()
                    res = False
                    break

        return res

    # [methodName arg1 arg2]
    def filterFlag(self, msgData="", fromName=""):
        res = True
        msgData = msgData.strip()
        flag = False
        size = len(msgData)
        msg = ""
        keys = ["别说话", "你别说话", "闭嘴", "shutup"]
        statusOn = ['笨蛋', '傻逼', 'sb', 'SB', 'Sb','sB', '傻b', '傻']
        statusOff = ['开心一点','开心点','我错了', '求你了', '后悔', '收回','我收回','对不起', '悔恨', '不要生气']


        if(not flag):
            for item in statusOff:
                if(msgData == item):
                    self.robot.turnUser(fromName, "0")
                    self.status = self.status + self.statusOnDeta
                    if(self.status >= self.statusMax + self.statusOnDeta):
                        msg = self.name + "现在没有生气(╯▔皿▔)╯"
                    elif(self.status >= self.statusDefault):
                        msg = self.name + "心情好转了 不生气了﹏"
                    else:
                        msg = self.name + "气消了一点点，生气值-" + str(self.statusOnDeta) + self.tail
                    flag = True
                    break
        if(self.robot.getUser(fromName).get("flag", "0") != "0"):   #限制黑名单只接受道歉
            res = True
            self.out("黑名单只接受道歉 不想搭理" + fromName)
            return res

        if(not flag):
            for item in keys:
                if(msgData == item):
                    self.status = self.status - self.statusDownDeta
                    msg = "好的" + ",生气值陡升" + str(self.statusDownDeta) + ",当前" + str(100-self.status) + "% "
                    flag = True
                    break
        if(not flag):
            for item in statusOn:
                if(msgData == item):
                    self.robot.turnUser(fromName, "1")
                    self.status = self.status - self.statusOffDeta
                    if(self.status <= self.statusMin - self.statusOffDeta):
                        msg = self.name + "已经气死了 没这号robot 😕"
                    elif(self.status <= self.statusMin):
                        msg = self.name + "已经气炸了 不想再说话了 ε=( o｀ω′)ノ "
                    else:
                        msg = self.name + "生气值暴涨" + str(self.statusOffDeta) + "，不想再搭理" + fromName + "了" + self.tail
                    flag = True
                    break

        if(flag):#状态控制
            self.out('filterFlag.' + str(flag) + "." + msgData)
            res = False
            self.send("/me " + msg)
        return res
    # methodName args eg: 'send aaaaa' 第一个空格分开函数名
    def doMethod(self, cmd):
        #music <on/off/turn/prev/next>
        cmd = cmd.strip()
        cmds = cmd.split(' ')
        if(len(cmds) > 0 and cmds[0] == ""):
            cmds.pop(0)
        listArgs = cmds
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
                    res = True
                    self.out(method)
        return res
    def let(self, attrName="", value=""):
        self.out("变量赋值." + str(attrName) + "." + str(value))
        if(hasattr(self, attrName)):
            method = getattr(self, attrName)#获取的是个对象
            if(callable(method)):
                self.out("该属性为方法")
            else:
                method = value
        else:
            self.out("该属性不存在")

    def shutdown(self):
        self.outRoom()

    def restart(self):
        self.shutdown()
        self.login()

    def test(self):
        self.login()
        self.getRooms()
        # self.goRoom("QGSNLntBvK")
        self.goRoomName("深海")
        # self.goARoom()
        ThreadRun( "DoSend." + str(self.count),  self.doHello ).start()
        ThreadRun( "SayHello." + str(self.count),  self.sayHello ).start()
        ThreadRun( "GetHello." + str(self.count),  self.getHello ).start()
        # ThreadRun( "InputHello." + str(self.count),  self.inputHello ).start()

        # for i in range(len(self.roomIndex.keys())):
        #     self.goRoom( self.roomIndex.keys()[i] )
        #     self.music("turn")
        #     time.sleep(7)
        #     self.outRoom()
        #     time.sleep(3)

        return

    def runStart(self):
        ThreadRun("Robot." + str(self.count),  self.runRobot).start()
    def runRobot(self):
        self.out("开始执行侵入:" + str(self.runIds))

        for i in self.runIds:
            room = self.makeRooms[i]
            roomId = room.get("id", "")
            self.out("侵入" + str(i) + " " + roomId )
            self.goRoom(roomId)
            self.playMusic()
            time.sleep(6)
            exitCount = 6
            while(exitCount >= 0):
                exitCount = exitCount - 1
                if(self.outRoom()):
                    break
                time.sleep(2)
            time.sleep(10)

        self.out("侵入完成:" + str(self.runIds))
def testCC():
    root = AutoSophia("cc", 0)
    root.test()

    tool.wait()

    return
def testMake():
    root = AutoSophia("白学家", -1)
    root.login()
    rooms = root.getRooms()
    #根据房间 筛选侵入目标
    ThreadRun( "InputHello." + str(root.count),  root.inputHello).start() #监控母体
    # roomsSorted = sorted(rooms, cmp=lambda x,y: cmp(x.get("name",""), y.get("name",""))   )
    # print(roomsSorted)
    i = 0
    makeRooms = []
    for room in rooms:
        id = room.get("id","")
        if(room.get("language","") == "zh-CN"):
            # root.showRoom(id, show=True, i=i)
            makeRooms.append(room)
        i = i + 1
    toSize = len(makeRooms) #侵入房间数量 37

    size = 10 #10个robot并行
    det = toSize / size
    if(size * det < toSize):
        det = det + 1   # 4
    print("共计房间" + str(toSize) + " 开启机器" + str(size) + " 每个执行任务" + str(det))
    objs = []
    st = 0
    for i in range(size):
        obj = AutoSophia("白学家0-" + str(i), i, makeRooms) # 白学家
        obj.login()
        obj.runIds = range(st, st + det)
        st = st + det
        objs.append(obj)
        time.sleep(0.5)
    print("Enter 下一步进入房间")
    # cmd=raw_input("")
    for i in range(size):
        objs[i].runStart()



    tool.wait()




if __name__ == '__main__':
    # testMake()
    testCC()
# the admin
# akakoori