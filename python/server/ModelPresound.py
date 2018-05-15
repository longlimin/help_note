#!/usr/bin/env python
#-*- coding:utf-8 -*- 
from include import *

#####################
from system import System

#####################
# 超声波模块
# VCC 5v 15mA
# GND
# TRIG  触发控制信号输入10uS TTL脉冲
# ECHO  回响输出    TTL电平

# 工作频率 40kHz
# 射程 2cm -> 4M
# 角度  15
# 尺寸  45x20x15mm


########################################
m_dc_default = 60
################################################
@singleton
class ModelPresound:
    def __init__(self):

        self.m_hz = 10            #pwm 0 : no pwm
        self.m_dc_start = 30
        self.m_dc_stop = 90s
        self.m_dc_default = (self.m_dc_start + self.m_dc_stop) / 2
        self.m_dc_now_left =  m_dc_default
        self.m_dc_now_right = m_dc_default
        self.m_dc_deta = 20
                            #rh黄-IN1  rb绿-IN2  lh蓝-IN3  lb红-IN4 39灰-地
        self.m_ports =      [31,       33,       35,       37]
        self.m_status =     [0, 0, 0, 0]    #端口使用状态  0关闭  / 1pwm开 / 2pwm关普通开

        self.setPorts(0, 0, 0, 0)


    def checkdist():
        GPIO.output(Trig_Pin, GPIO.HIGH)
        time.sleep(0.00015)
        GPIO.output(Trig_Pin, GPIO.LOW)
        while not GPIO.input(Echo_Pin):
            pass
        t1 = time.time()
        while GPIO.input(Echo_Pin):
            pass
        t2 = time.time()
        return (t2-t1)*340*100/2



# init
ModelMove()
