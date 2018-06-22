#!/usr/bin/python
#-*- coding:utf-8 -*-  
import urllib2 



"""
General
    Request URL:http://drrr.com/
    Request Method:GET
    Status Code:200 OK
    Remote Address:23.251.96.131:80
    Referrer Policy:no-referrer-when-downgrade
Response Headers view source
    Access-Control-Allow-Credentials:true
    Access-Control-Allow-Origin://drrr.com
    Cache-Control:no-cache
    Connection:keep-alive
    Content-Encoding:gzip
    Content-Type:text/html; charset=UTF-8
    Date:Fri, 22 Jun 2018 10:24:55 GMT
    Expires:Fri, 22 Jun 2018 10:24:54 GMT
    Pragma:no-cache
    Server:nginx
    Strict-Transport-Security:max-age=86400; includeSubDomains; preload
    Transfer-Encoding:chunked
    Vary:Accept-Encoding
    X-Cache:MISS from 001.mul.lax01.us.krill.zenlogic.net
    X-ORCA-Accelerator:MISS from 001.mul.lax01.us.krill.zenlogic.net
Request Headers view source
    Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding:gzip, deflate
    Accept-Language:zh-CN,zh;q=0.9
    Cache-Control:no-cache
    Connection:keep-alive
    Cookie:_ga=GA1.2.1468643479.1529641802; _gid=GA1.2.1221378764.1529641802; drrr-session-1=lsi8ru9ciedcibkl7kcg78ujo5; _gat=1
    DNT:1
    Host:drrr.com
    Pragma:no-cache
    Referer:http://drrr.com/lounge
    Upgrade-Insecure-Requests:1
    User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
"""


  
# 设置浏览器请求头  
headers={  
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9",
    "Cache-Control":"no-cache",
    "Connection":"keep-alive",
    "Cookie":"_ga=GA1.2.1468643479.1529641802; _gid=GA1.2.1221378764.1529641802; drrr-session-1=lsi8ru9ciedcibkl7kcg78ujo5; _gat=1",
    "DNT":"1",
    "Host":"drrr.com",
    "Pragma":"no-cache",
    "Referer":"http://drrr.com/lounge",
    "Upgrade-Insecure-Requests":"1",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}  
  
#建立请求内容  
request=urllib2.Request("http://drrr.com",headers=headers)  
  
#获取响应  
response=urllib2.urlopen(request)  
  
#页面内容  
html=response.read()  
  
# print html  

print response.getcode() #返回响应码  
print response.geturl() #返回实际url  
print response.info() #返回服务器响应的报头  
print "---------------"
print(response)
fo = open("/mnt/e/test.html", "w")
fo.write(html.toString())

if __name__ == '__main__':
    pass
    # AutoSophia()

        