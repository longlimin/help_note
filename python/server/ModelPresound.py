#!/usr/bin/env python
#-*- coding:utf-8 -*- 
from include import *

#####################
from system import System

#####################
# 超声波模块
# 前进      左右前
# 后退      左右退

########################################
m_dc_default = 60
################################################
@singleton
class ModelPresound:
    def __init__(self):

        self.m_hz = 10            #pwm 0 : no pwm
        self.m_dc_start = 30
        self.m_dc_stop = 90
        self.m_dc_default = (self.m_dc_start + self.m_dc_stop) / 2
        self.m_dc_now_left =  m_dc_default
        self.m_dc_now_right = m_dc_default
        self.m_dc_deta = 20
                            #rh黄-IN1  rb绿-IN2  lh蓝-IN3  lb红-IN4 39灰-地
        self.m_ports =      [31,       33,       35,       37]
        self.m_status =     [0, 0, 0, 0]    #端口使用状态  0关闭  / 1pwm开 / 2pwm关普通开

        self.setPorts(0, 0, 0, 0)



# init
ModelMove()
