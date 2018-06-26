#!/usr/bin/python
#-*- coding:utf-8 -*-  
 
import json
import time
import BeautifulSoup
import tool
from http import Http

class AutoSophia:
    def __init__(self, name="00000"):
        self.roomIndex = {}
        self.http = Http()
        self.name = name
    def out(self, obj):
        print(self.name + "." + obj)
    def login(self):
        tool.line()
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

            tool.line()
            self.out("模拟登录")
            responce=self.http.doPost('http://drrr.com/', {
                        "name":self.name,
                        "login":"ENTER",
                        "token":token,
                        "direct-join":"",
                        "language":"zh-CN",
                        "icon":"zaika",
                })
        else:
            self.out("error！ 没能抓取到token")

    def goRoom(self, roomId):
        tool.line()
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
            roomIndex[room["id"]] = room
            self.out("#" + str(i) + "\t" + room["id"] + " " + str(room["total"]) + "/" + str(room["limit"]) + "\t " + room["name"])
        self.out("解析完毕")
    def sayHello(self):
        tool.line()

        for i in range(600):
            message = "现在的时间是："+ time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            print(str(i) + "\t" + message)
            r=self.http.doPost("http://drrr.com/room/?ajax=1", {
                        "message":message,
                        "url":"",
                })
            time.sleep(60)

    def test(self):
        self.login()
        # self.getRooms()
        self.goRoom("Abe7gATu1w") # roomIndex.keys()[0])
        self.sayHello()

if __name__ == '__main__':
    robot = AutoSophia("zaika")
    robot.test()