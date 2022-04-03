#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/18 21:34
# @Author : WangZihang
# @Function : 用于释放树莓派所有GPIO接口

import RPi.GPIO as GPIO
import car_init

init = car_init.init()
GPIO.output(init.motor_A_A, GPIO.LOW)
GPIO.output(init.motor_A_B, GPIO.LOW)
GPIO.output(init.motor_B_A, GPIO.LOW)
GPIO.output(init.motor_B_B, GPIO.LOW)
GPIO.output(init.motor_C_A, GPIO.LOW)
GPIO.output(init.motor_C_B, GPIO.LOW)
GPIO.output(init.motor_D_A, GPIO.LOW)
GPIO.output(init.motor_D_B, GPIO.LOW)

import RPi.GPIO as GPIO
GPIO.cleanup()
