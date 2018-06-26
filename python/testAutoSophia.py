#!/usr/bin/python
#-*- coding:utf-8 -*-  

import tool
from autoSophia import AutoSophia
from tool import ThreadRun
import time

size = 10
objs = []
for i in range(size):
    obj = AutoSophia("Walker" + str(i))
    objs.append(obj)
for i in range(size):
    ThreadRun(
        "Robot." + str(i), 
        objs[i].test
    ).start()
    time.sleep(1)



while True:
    pass