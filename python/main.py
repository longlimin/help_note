#!/usr/bin/python
#-*- coding:utf-8 -*-   

from template import *

class main:
    """A main class"""  

    def __init__(self):

        template = Template()
        template.set("001", "walker")
        res = template.toString()
        print(res)
        








main()


