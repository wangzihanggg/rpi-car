#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/18 21:10
# @Author : WangZihang
# @Function :对树莓派GPIO接口进行初始化

import RPi.GPIO as GPIO



class init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    motor_A_A = 8  # 命名规则电机_序号_驱动板引脚  赋值=GPIO引脚
    motor_A_B = 7
    motor_B_A = 11
    motor_B_B = 13
    motor_C_A = 19
    motor_C_B = 21
    motor_D_A = 16
    motor_D_B = 18

    echo = 24
    trig = 26
    # 电机 L9110s
    GPIO.setup(motor_A_A, GPIO.OUT)
    GPIO.setup(motor_A_B, GPIO.OUT)
    GPIO.setup(motor_B_A, GPIO.OUT)
    GPIO.setup(motor_B_B, GPIO.OUT)
    GPIO.setup(motor_C_A, GPIO.OUT)
    GPIO.setup(motor_C_B, GPIO.OUT)
    GPIO.setup(motor_D_A, GPIO.OUT)
    GPIO.setup(motor_D_B, GPIO.OUT)

    # 超声波 HC-SR04
    GPIO.setup(trig, GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(echo, GPIO.IN)



    '''
            wheel_spin_direction
            GO_AHEAD
            motorA A1 B0
            motorB A0 B1
            motorC A0 B1
            motorD A1 B0
    '''

