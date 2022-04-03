#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/18 21:17
# @Author : WangZihang
# @Function : 对小车进行运动测试
import time
import Ultrasonic
import car_move as move
import Ultrasonic
def move_test1():
    time.sleep(1)
    move.car_move_forward()
    time.sleep(1)
    move.car_stop()
    time.sleep(1)
    move.car_move_backward()
    time.sleep(1)
    move.car_stop()
    time.sleep(1)
    move.car_turn_left()
    time.sleep(1)
    move.car_stop()
    time.sleep(1)
    move.car_turn_right()
    time.sleep(1)
    move.car_stop()
    time.sleep(1)
    move.car_left_parallel()
    time.sleep(0.5)
    move.car_stop()
    time.sleep(1)
    move.car_right_parallel()
    time.sleep(0.5)
    move.car_stop()

def move_test2():
    while True:
        dis = Ultrasonic.start_Ultrasonic()
        if dis < 50:
            move.car_stop()
        else:
            move.car_move_forward()





