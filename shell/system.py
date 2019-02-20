#!/usr/bin/python
#-*- coding:utf-8 -*-

import os,sys,time,uuid,json,threading,random

def makeArray(cmd, length, split=":"):
    res=exe(cmd)
    resList=[]
    arr=res.split("\n")
    for item in arr:
        cols=item.split(split)
        if(len(cols) != length):
            #print("err", cols)
            continue
        resList.append(cols) 
    return resList
def showArray(arr, sub="", title=[], orderBy=0):
    resList = sorted(arr, cmp=lambda x,y: cmp(x[orderBy], y[orderBy])   )
    print("\n" + sub)
    sstr=""
    for item in title:
        sstr=sstr + str(item) + " \t"
    print(sstr)
    for obj in arr:
        sstr=""
        for i in range(0, len(title)):
            sstr=sstr + str(obj[i]) + " \t"
        print(sstr)
def exe(str):
    return os.popen(str).read().encode("utf-8")
def getNowTime():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    
def showNetstat():
    arr=makeArray("netstat -ano | grep tcp | awk '{print $4,$5}' OFS=':' ", 4)
    all=0
    map={}
    for cols in arr:
        toip=cols[2]
        toport=cols[3]
        fromip=cols[0]
        fromport=cols[1]
        obj=map.get(toip, {})
        count=obj.get("count", 0)
        ports=obj.get("ports", [])
        count+=1
        all+=1 
        ports.append(fromport)
        obj["count"]=count
        obj["ports"]=ports
        obj["toip"]=toip
        map[toip]=obj
    resList = sorted(map.values(), cmp=lambda x,y: cmp(x["count"], y["count"])   )
    resList.insert(0, { "toip":"toip       ", "count":"count", "ports":["ports"] } )
    print("\nNetstat")
    for item in resList:
        print(str(item["toip"]) + " \t" +str(item["count"]) + " \t" + str(item["ports"][0:5]) )
    print("All num : " + str(all))
    
def showDisk():
    arr=makeArray("df -h | grep -v loop | grep -v tmpfs | awk 'NR!=1{print $2,$5,$1,$6}' OFS=':' ", 4)
    showArray(arr, "Disk", ("All", "Now", "FileSys", "Mount") )

def showMem():
    arr=makeArray("free -h | awk 'NR!=1{print $2,$3,$7}' OFS=':' ", 3)
    showArray(arr, "Memory", ("All", "Now", "Free") )


print("展示系统属性 netstat top<cpu mem> disk " + getNowTime() )
showNetstat()
showMem()
showDisk()





