#!/usr/bin/env python
#-*- coding:utf-8 -*-  
import tornado.ioloop
import tornado.web  
import tornado.httpserver  
import sys

#####################self

from HandlerTest import HandlerTest
from HandlerStudent import HandlerStudent
from HandlerSystem import HandlerSystem




#####################



application = tornado.web.Application([ 

    (r"/", HandlerTest),
    (r"/+do/+student/+(?P<method>.+)/+(?P<params>.*)", HandlerStudent),
    (r"/+do/+system/+(?P<method>.+)/+(?P<params>.*)", HandlerSystem), #非raspberry上运行需要屏蔽此服务






])

'''
1、在路由映射条件里用正则匹配访问路径后缀
2、给每一个正则匹配规则(?P<设置名称>)设置一个名称，
3、在逻辑处理的get()方法或post()方法，接收这个正则名称，就会接收到用户访问的后缀路径
'''

if __name__ == "__main__":
    print("Start server http ")
    application.listen(8086)
    tornado.ioloop.IOLoop.instance().start()



