#!/usr/bin/env python
#-*- coding:utf-8 -*-  
import json
import os
import sys

sys.path.append("./opencv/")
sys.path.append("./server/")
########################################
# from cv_makecolor import MakeColor

############################

class Tool:
    """A tool class   and include imort all the need files""" 

    def __init__(self):
        self.id = "test id"
        self.name = "test name"


    #exe the shell cmd, return the string encode by utf-8
    @staticmethod
    def exe(str):
        # (status, output) = commands.getstatusoutput(str)
        # return output
        return os.popen(str).read().encode('utf-8') 





















        