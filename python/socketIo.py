from socketIO_client import SocketIO

import sys
import os
import json
import re
import codecs
import time
import threading
import thread
import yaml
import uuid
import base64
import tool
import traceback


class Socket:
    def __init__(self, url, port):
        self.socket = None

        self.url = url
        self.port = port


        self.connect()
        self.startThreadRead()
        # self.socket.wait_for_callbacks(seconds=1)
        return
    def connect(self):
        self.out("Connect url:" + self.url + " port:" + str(self.port))
        self.socket = SocketIO(self.url,port=self.port) # , params=self.config)
        self.out("Connect over ")
        return
    def send(self, type, data, callback=None):
        if(self.socket == None):
            self.connect()
        self.out("send:")
        self.out("type:" + type)
        self.out("data:" + str(data))

        self.socket.emit(type, data, callback)
        return
    def startThreadRead(self):
        while(True):
            if(self.socket != None):
                self.out("开启线程等待读取")
            while(self.socket != None):
                try:
                    self.socket.wait()
                except Exception as e:
                    self.out(traceback.format_exc())
                time.sleep(1)
            time.sleep(3)

        return

    def on(self, item, method):
        self.socket.on(item, method)
        return
    def out(self, obj):
        print("socketio." + str(obj))



















def test():
    hosts = 'cochat.cn'
    port = 9091

    # 收到message消息处理过程
    def on_message(*args):
        print ("recv:", args)

    sk = SocketIO(hosts,port=port)
    # sk = SocketIO(hosts,port=port,params={'token': 'ksdjfkjdf'})  #create connection with params

    # add lisenter for message response
    sk.on('message', on_message)

    data = {
        "v1": "aaaaaaaaaaa",
        "v2": "bbbbbbbbb"}
    # send data to message
    sk.emit('message', data, on_message)
    # sk.sendf(data, on_message) # default send data to message
    #send data to login
    sk.emit('event', data, on_message)

    print("over")
    sk.wait_for_callbacks(seconds=1)
