#!/usr/bin/python
#-*- coding:utf-8 -*-  
import urllib
import urllib2
import cookielib

def httpGet(name, url, data):
    print(name)
    # 模拟登录，并把cookie保存到变量
    try:
        if(data):
            result = opener.open(url, urllib.urlencode(data))
        else:
            result = opener.open(url)
        show(result)
    except Exception as e:
        print(e)
    show(result)


# print("登录认证")
# # 模拟登录，并把cookie保存到变量
# result = opener.open("http://drrr.com/",
#     urllib.urlencode({
#             "name":"Walker004",
#             "login":"ENTER",
#             "token":"0e2ebc572e16d8f983f5a399b54e8823",
#             "direct-join":"",
#             "language":"zh-CN",
#             "icon":"eight",
#     })
# )
# show(result)


def show(result):
    try:
        print(result.read())
    except Exception as e:
        print(e)
    print("\n------------------------------------\n")

filename = 'cookie.txt'
# 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))

print("访问主页")
result = opener.open("http://drrr.com/")
cookie.save(ignore_discard=True, ignore_expires=True)

show(result)
httpGet("登录认证", "http://drrr.com/", {
            "name":"Walker004",
            "login":"ENTER",
            "token":"0e2ebc572e16d8f983f5a399b54e8823",
            "direct-join":"",
            "language":"zh-CN",
            "icon":"eight",
    })
 
# 保存cookie到cookie.txt中
cookie.save(ignore_discard=True, ignore_expires=True)

httpGet("获取房间列表", "http://drrr.com/lounge?api=json")

httpGet("加入房间", "http://drrr.com/room/?id=cgyRhaqTvB")
 




print("等待------")
while(True):
    pass

