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
        self.socket.on('message', on_message)

        self.out("Connect over ")
        return
    def emit(self, type, data, callback=None):
        return self.send(type, data, callback)
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
                    self.out("wait")
                    self.socket.wait(1)
                except Exception as e:
                    self.out(traceback.format_exc())
                # time.sleep(1)
            time.sleep(1)

        return

    def on(self, item, method):
        self.socket.on(item, method)
        return
    def out(self, obj):
        print("socketio." + str(obj))














def t():
    hosts = 'cochat.cn'
    port = 9091
    socket = Socket(hosts, port)
    socket.on('message', on_message)
    socket.on('error', on_error)
    data = {
        "v1": "aaaaaaaaaaa",
        "v2": "bbbbbbbbb"}
    socket.emit('message', data, messageCall)
    socket.emit('event', data, eventCall)

    time.sleep(1)
    tool.wait()

def messageCall(args):
    print("messageCall---------")
    print(args)
    print("-------------")
def eventCall(args):
    print("eventCall---------")
    print(args)
    print("-------------")
def on_error(args):
    print("on_error---------")
    print(args)
    print("-------------")
# 收到message消息处理过程
def on_message(args):
    print("on_message---------")
    print(args)
    print("-------------")
def test():
    hosts = 'cochat.cn'
    port = 9091


    sk = SocketIO(hosts,port=port)
    # sk = SocketIO(hosts,port=port,params={'token': 'ksdjfkjdf'})  #create connection with params

    # add lisenter for message response
    sk.on('message', on_message)

    data = {
        "v1": "aaaaaaaaaaa",
        "v2": "bbbbbbbbb"}
    sk.emit('message', data, messageCall)
    # sk.emit('event', data, eventCall)
    print("over")
    # sk.wait_for_callbacks(seconds=1)
    sk.wait()
    tool.wait()




if __name__ == '__main__':
    t()