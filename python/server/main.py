#!/usr/bin/env python
#-*- coding:utf-8 -*-   
 

# 包含文件导入所有 
from include import *

@singleton
class main:
    """A main class"""  

    def __init__(self):
        print('init main')
        # 普通类使用
        template = Template()
        template.set("001", "walker")
        res = template.toString()
        print(res)
        template = Template()
        print(template.toString())

        # 模块
        testModel.set('setid', 'setname')
        print(testModel.toString())

        print(tool.exe('uptime'))









main()
main()

