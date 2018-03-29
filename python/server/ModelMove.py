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
        self.m_ports =  [31, 33, 35, 37]
        self.m_status = [0, 0, 0, 0]

        self.setPorts(0, 0, 0, 0)



#开启或关闭0/1 
    def setMovePort(self, cc, value):
        System().setPort(self.m_ports[cc], value)
        self.m_status[cc] = value

#开启或关闭pwm/0
    def setMovePortPwm(self, cc, value = 0, dc = m_dc_default):
        if(value == 1):
            if(dc > self.m_dc_stop):
                res, info = System().closePortPwm(self.m_ports[cc])
                print(res, info)
                res, info = System().setPort(self.m_ports[cc], value)
                print(res, info)
            else:
                res, info = System().openPortPwm(self.m_ports[cc], self.m_hz, dc)
                print(res, info)
            self.m_status[cc] = dc
        else:
            res, info = System().closePortPwm(self.m_ports[cc])
            print(res, info)
            res, info = System().setPort(self.m_ports[cc], value)
            print(res, info)

            self.m_status[cc] = 0

#改变pwm 调速dc 0/100
    def updateMovePortPwm(self, cc, dc = m_dc_default):
        System().setPortPwm(self.m_ports[cc], self.m_hz, dc)

# 根据values状态控制移动状态
    def setPorts(self, *values): 
        self.setMovePortPwm(0, values[0], self.m_dc_now_left)
        self.setMovePortPwm(1, values[1], self.m_dc_now_left)

        self.setMovePortPwm(2, values[2], self.m_dc_now_right)
        self.setMovePortPwm(3, values[3], self.m_dc_now_right)
# 根据新修改过的dc left/right更新pwm if已经开启了pwm
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
        res = 0
        for ss in self.m_status:
            res = (res + ss ) * 10
        return res

    def moveHead(self):
        self.space()
        #lb  lh  rb  rh
        self.setPorts(0, 1, 0, 1) 

    def moveBack(self):
        self.space()
        #lb  lh  rb  rh
        self.setPorts(1, 0, 1, 0) 

    def turnLeft(self):
        self.space()

        #lb  lh  rb  rh
        self.setPorts(1, 1, 0, 1)

    def turnRight(self):
        self.space()

        #lb  lh  rb  rh
        self.setPorts(0, 1, 1, 1) 

    def stop(self):
        self.space()

        # self.setPorts(1, 1, 1, 1)   #1111

    def space(self):
        self.setPorts(0, 0, 0, 0)  #0


ModelMove()
