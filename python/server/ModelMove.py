#!/usr/bin/env python
#-*- coding:utf-8 -*- 
from include import *

#####################
from system import System

#####################
# //H桥电机模块
# 前进      左右前
# 后退      左右退

# 左转      左空置 右前
#             左后退     右空置
#             左后退 又前

# 右转
# 左刹车
# 右刹车
# 左空置
# 右空置

#         IN1     IN2     IN3      IN4
# 左前  1/pwm   0       
# 左退  0       1/pwm
# 左空置 0       0
# 左刹车 1       1
########################################
m_dc_default = 60
################################################
@singleton
class ModelMove:
    def __init__(self):

        self.m_hz = 10            #pwm 0 : no pwm
        self.m_dc_start = 30
        self.m_dc_stop = 90
        self.m_dc_default = (self.m_dc_start + self.m_dc_stop) / 2
        self.m_dc_now_left =  m_dc_default
        self.m_dc_now_right = m_dc_default
        self.m_dc_deta = 20
                        #lb  lh  rb  rh
        self.m_ports =      [31, 33, 35, 37]
        self.m_status =     [0, 0, 0, 0]    #端口使用状态  0关闭  / 1pwm开 / 2pwm关普通开

        self.setPorts(0, 0, 0, 0)


    def openPortPwm(self, port, hz, dc):
# pwm/非pwm开关控制 
# port[0] value=1 dc=80
# port[1] value=1 dc=90
    def setMovePortPwm(self, cc, value = 0, dc = m_dc_default):
        print('setMovePortPwm', self.m_ports[cc], value, dc)
        if(value == 1): #打开
            if(dc >= self.m_dc_stop):   #无需pwm
                if(self.m_status[cc] == 0):     #关闭状态
                    res, info = System().setPort(self.m_ports[cc], value)   #开启端口
                    self.m_status[cc] = 2 
                elif(self.m_status[cc] == 1):   #pwm开启状态
                    res, info = System().closePortPwm(self.m_ports[cc])     #关闭pwm
                    print(res, info)
                    self.m_status[cc] = 0 
                    res, info = System().setPort(self.m_ports[cc], value)   #开启端口
                    self.m_status[cc] = 2 
                elif(self.m_status[cc] == 2):   #已经开启端口
                    res = False
                    info = 'have open port ' + str(self.m_ports[cc])        #不操作
            else:                       #需要pwm
                if(self.m_status[cc] == 0):     #关闭状态
                    res, info = System().openPortPwm(self.m_ports[cc], self.m_hz, dc)     #开启pwm
                    self.m_status[cc] = 1 
                elif(self.m_status[cc] == 1):   #pwm开启状态
                    res = False
                    info = 'have open pwm ' + str(self.m_ports[cc])        #不操作
                elif(self.m_status[cc] == 2):   #已经开启端口
                    res, info = System().closePort(self.m_ports[cc])     #关闭端口
                    print(res, info)
                    self.m_status[cc] = 0
                    res, info = System().openPortPwm(self.m_ports[cc], self.m_hz, dc)     #开启pwm
                    self.m_status[cc] = 1 
        else:       #关闭
            if(self.m_status[cc] == 0):     #关闭状态
                res, info = System().closePort(self.m_ports[cc])        #不操作 再确认关闭端口
            elif(self.m_status[cc] == 1):   #pwm开启状态
                res, info = System().closePortPwm(self.m_ports[cc])     #关闭pwm
                self.m_status[cc] = 0 
            elif(self.m_status[cc] == 2):   #已经开启端口
                res, info = System().closePort(self.m_ports[cc])     #关闭端口
                self.m_status[cc] = 0 

        print(res, info)

# pwm 更新 调速dc 0/100
    def updateMovePortPwm(self, cc, dc = m_dc_default):
        print('updateMovePortPwm', cc, dc)

        if(dc >= self.m_dc_stop):   #无需pwm
            if(self.m_status[cc] == 1):   #pwm开启状态
                res, info = System().closePortPwm(self.m_ports[cc])     #关闭pwm
                print(res, info)
                self.m_status[cc] = 0 
                res, info = System().setPort(self.m_ports[cc], value)   #开启端口
                self.m_status[cc] = 2 
            elif(self.m_status[cc] == 2):   #已经开启端口
                res = False
                info = 'have update to open port ' + str(self.m_ports[cc])        #不操作
        else:                       #需要pwm
            if(self.m_status[cc] == 1):   #pwm开启状态
                res, info = System().setPortPwm(self.m_ports[cc], self.m_hz, dc)    #更新pwm
            elif(self.m_status[cc] == 2):   #已经开启端口
                res, info = System().closePort(self.m_ports[cc])     #关闭端口
                print(res, info)
                self.m_status[cc] = 0
                res, info = System().openPortPwm(self.m_ports[cc], self.m_hz, dc)     #开启pwm
                self.m_status[cc] = 1 
        print(res, info)

# 根据values状态控制移动状态
    def setPorts(self, *values): 
        self.setMovePortPwm(0, values[0], self.m_dc_now_left)
        self.setMovePortPwm(1, values[1], self.m_dc_now_left)

        self.setMovePortPwm(2, values[2], self.m_dc_now_right)
        self.setMovePortPwm(3, values[3], self.m_dc_now_right)
# 根据新修改过的dc left/right更新速度 90dc上下修改pwm为端口开闭
    def updatePorts(self): 
        self.updateMovePortPwm(0, self.m_dc_now_left)
        self.updateMovePortPwm(1, self.m_dc_now_left)

        self.updateMovePortPwm(2, self.m_dc_now_right)
        self.updateMovePortPwm(3, self.m_dc_now_right)
# 速度调控 快 慢 分档 dc 0-100
    def moveFaster(self, flag = 1):
        self.m_dc_now_right = self.m_dc_now_right + self.m_dc_deta * flag
        if(self.m_dc_now_right < self.m_dc_start):
            self.m_dc_now_right = self.m_dc_start
        elif(self.m_dc_now_right > self.m_dc_stop):
            self.m_dc_now_right = self.m_dc_stop

        self.m_dc_now_left = self.m_dc_now_left + self.m_dc_deta * flag
        if(self.m_dc_now_left < self.m_dc_start):
            self.m_dc_now_left = self.m_dc_start
        elif(self.m_dc_now_left > self.m_dc_stop):
            self.m_dc_now_left = self.m_dc_stop

        self.updatePorts()

    def getStatus(self):
        res = ''
        for ss in self.m_status:
            res = res + str(ss)
        return res

    def moveHead(self):
        #lb  lh  rb  rh
        self.setPorts(0, 1, 0, 1) 

    def moveBack(self):
        #lb  lh  rb  rh
        self.setPorts(1, 0, 1, 0) 

    def turnLeft(self):

        #lb  lh  rb  rh
        self.setPorts(1, 1, 0, 1)

    def turnRight(self):

        #lb  lh  rb  rh
        self.setPorts(0, 1, 1, 1) 

    def stop(self):
        self.setPorts(1, 1, 1, 1)   #1111

    def space(self):
        self.setPorts(0, 0, 0, 0)  #0


ModelMove()
