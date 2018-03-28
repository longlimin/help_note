#!/usr/bin/env python
#-*- coding:utf-8 -*- 


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

m_hz = 20            #pwm 0 : no pwm
m_dc_start = 30
m_dc_stop = 100
m_dc_default = (m_dc_start + m_dc_stop) / 2
m_dc_now_left =  m_dc_default
m_dc_now_right = m_dc_default
m_dc_deta = 20

m_ports =  [22, 23, 24, 25]
m_status = [0, 0, 0, 0]

################################################
class ModelMove:
    
#开启或关闭0/1 
    @staticmethod
    def setMovePort(cc, value):
        System.setPort(m_ports[cc], value)

#开启或关闭pwm/0
    @staticmethod
    def setMovePortPwm(cc, value = 0, dc = m_dc_default):
        if(value == 1):
            System.openPortPwm(m_ports[cc], m_hz, dc)
        else:
            System.closePortPwm(m_ports[cc])

#改变pwm 调速dc 0/100
    @staticmethod
    def updateMovePortPwm(cc, dc = m_dc_default):
        System.setPortPwm(m_ports[cc], m_hz, dc)
   
    @staticmethod
    def setPorts(values):
        i = 0

        if(m_dc_now > 90): #不调速
            for value in values :
                setMovePort(m_ports[i], value)
                i = i + 1
        else:
            setMovePortPwm(m_ports[i], values[i], m_dc_now_left)
            i = i + 1
            setMovePortPwm(m_ports[i], values[i], m_dc_now_left)
            i = i + 1
            setMovePortPwm(m_ports[i], values[i], m_dc_now_right)
            i = i + 1
            setMovePortPwm(m_ports[i], values[i], m_dc_now_right)

    @staticmethod
    def init():
        setPorts(0, 0, 0, 0)

# 速度调控 快 慢 分档 dc 0-100
    @staticmethod
    def moveFaster(dc):
        m_dc_now_right = m_dc_now_right + m_dc_deta
        if(m_dc_now_right < m_dc_start):
            m_dc_now_right = m_dc_start
        elif(m_dc_now_right > m_dc_stop):
            m_dc_now_right = m_dc_stop

        m_dc_now_left = m_dc_now_left + m_dc_deta
        if(m_dc_now_left < m_dc_start):
            m_dc_now_left = m_dc_start
        elif(m_dc_now_left > m_dc_stop):
            m_dc_now_left = m_dc_stop

    @staticmethod
    def moveHead():
        setPorts(0, 1, 0, 1) 

    @staticmethod
    def moveBack():
        setPorts(1, 0, 1, 0) 

    @staticmethod
    def turnLeft():
        setPorts(0, 1, 1, 1)

    @staticmethod
    def trunRight():
        setPorts(1, 1, 1, 0) 





