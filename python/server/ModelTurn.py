#!/usr/bin/env python
#-*- coding:utf-8 -*- 


#####################
from system import System

#####################
# //舵机转向模块
# 红vcc
# 橙信号
# 灰gnd
#
# 转动规则 pwm 
# 频率 50hz / T:20ms
# 转动角度    周期内持续时间
# 
# 
########################################
# 20ms周期中 调整dc以控制角度 dc=k角度 dc的持续变动非跃迁 以实现角度的持续变动    T=T20+sleep
#                                      1-sleep-2-sleep-3-sleep-4-sleep-5          10 20 30 40 50 
t_port = 23
t_hz = 50           #20ms 周期 1s 50T 舵机需要周期决定 
t_t = 1000 / t_hz   #T 20ms
t_count = 75        #转动180d 需要变换100c  最快变换速度1s/50c -> 2s移动完毕

t_time_default = 4000       #转动180d 4s 控制速度   最快(20+2)*t_count ms
t_sleep_min = 0.002         # s最小延时 2ms
t_sleep_default = (t_time_default / t_count - 1000 / t_hz) / 1000.0 #0.020  4000ms/100c=1000ms/50c + sleep:20ms
t_min_time = (1000 / t_hz + t_sleep_min) * t_count  # 最小180d变换时间 ms


# dc 
t_dc_start = 0                                            #最小dc
t_dc_stop = 15
# t_dc_default = (t_dc_start + t_dc_stop) / 2               #默认dc
t_dc_deta = 1.0 * (t_dc_stop - t_dc_start) / t_count      #最小转动dc差值 16/80=0.2
# t_dc_now = t_dc_default

# degree 度数定义
t_start = 0                             #最小度数
t_stop = 180
t_default = (t_start + t_stop) / 2
t_deta = 1.0 * (t_stop - t_start) / t_dc_deta   #最小转动度数
t_now = t_default

t_turn_degree2dc =  (t_dc_stop - t_dc_start) / (t_stop - t_start) #12 转换degree为dc 0/15 y 0/180 x         y = 12*x + t_dc_start
  
##############################################
class ModelMove:

# default位置角度 
    @staticmethod
    def init():
        return turnTo()


# 转至指定角度 45 90 135 移动速度3000
    @staticmethod
    def turnTo(toDegree = t_default, speed = t_time_default):
        detaDegree = toDegree - t_now
        return turnDeta(detaDegree, speed)

# 相对现在转一定角度 增加度数/减少度数 移动速度:3000ms 转动180d耗时
    @staticmethod
    def turnDeta(detaDegree = 0, speed = t_time_default):
        costTime = 0
        (ifMove, dcMoveFrom, dcMoveTo, toDegree, info) = calcTurn(detaDegree)
        t_now = toDegree    #更新当前度数为预期度数

        print('操作: ' + info)
        if(ifMove):
            sleepTime = calcSpeed(speed)
            # port, hz, dcFrom, dcTo, dcDeta, sleepTime
            costTime = System.controlPwmAsync(t_port, t_hz, dcMoveFrom, dcMoveTo, t_dc_deta, sleepTime)
            t_dc_now = dcMoveTo  #更新当前dc为新dc

        print('耗时: ' + str(costTime))
        return (ifMove, info, sleepTime)


# 计算 速度对应的sleep时间 计算周期以此控制周期频率 控制转动速度
    @staticmethod
    def calcSpeed(speed):
        if(speed <= t_min_time):
            sleepTime = t_sleep_min #最快速度 sleep
        else:
            sleepTime = (speed / t_count - 1000 / t_hz) / 1000.0 #0.020  4000ms/100c=1000ms/50c + sleep:20ms
        return sleepTime

# 计算 转动角度后的预期 结果 from to pEnd info 并转换为dc制
# return (是否需要移动, fromDc, toDc, toDegree, 说明)
    @staticmethod
    def calcTurn(degree = 0):
        ifOk = False        
        info = ''
        if(degree > 0): #右转 增加度数
            if(t_now < t_stop):
                if(t_now + degree > t_stop):    #转动结果度数大于了最大度数
                    pEnd = t_stop
                    info = '转向到(最大): ' + str(pEnd)
                else:
                    pEnd = t_now + degree
                    info = '转向到: ' + str(pEnd)
            else:
                pEnd = t_now
                info = '已经转向到最大: ' + str(pEnd)
        else:       #左转 减少度数
            if(t_now > t_start):
                if(t_now + degree < t_start):   #小于了最小度数
                    pEnd = t_start
                    info = '转向到(最小): ' + str(pEnd)
                else:
                    pEnd = t_now + degree
                    info = '转向到: ' + str(pEnd)
            else:
                pEnd = t_now
                info = '已经转向到最小: ' + str(pEnd)


        if(pEnd == t_now):  #无操作
            info = '无操作 ' + info
        else:
            info = '从: ' + str(t_now) + ' ' + info
            ifOk = True

        dcMoveF = t_now * t_turn_degree2dc + t_dc_start
        dcMoveT = pEnd * t_turn_degree2dc + t_dc_start

        return (ifOk, dcMoveF, dcMoveT, pEnd, info)




