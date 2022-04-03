#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/18 21:32
# @Author : WangZihang
# @Function : 车载超声波测距

import RPi.GPIO as GPIO
import time
import car_init

init = car_init.init()


def start_Ultrasonic():
    while 1:
        # 超声波测量部分
        GPIO.output(init.trig, True)
        time.sleep(0.00011)  # 发送1us的信号
        GPIO.output(init.trig, False)

        # start recording
        while GPIO.input(init.echo) == 0:
            pass
        start = time.time()

        # end recording
        while GPIO.input(init.echo) == 1:
            pass
        end = time.time()

        # compute distance  根据时间，计算出声的传播速度/2即为距离
        distance = round((end - start) * 343 / 2 * 100, 2)
        print("distance:{0}cm".format(distance))
        return distance
        time.sleep(0.5)
