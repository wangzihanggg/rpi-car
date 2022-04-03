#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/1/18 21:15
# @Author : WangZihang
# @Function : 控制小车移动方向函数

import RPi.GPIO as GPIO
import car_init

init = car_init.init()

def car_move_forward():                      #小车向前运动
    GPIO.output(init.motor_A_A, GPIO.HIGH)
    GPIO.output(init.motor_A_B, GPIO.LOW)
    GPIO.output(init.motor_B_A, GPIO.LOW)
    GPIO.output(init.motor_B_B, GPIO.HIGH)
    GPIO.output(init.motor_C_A, GPIO.LOW)
    GPIO.output(init.motor_C_B, GPIO.HIGH)
    GPIO.output(init.motor_D_A, GPIO.HIGH)
    GPIO.output(init.motor_D_B, GPIO.LOW)

def car_move_backward():                        #小车向后运动
    GPIO.output(init.motor_A_A, GPIO.LOW)
    GPIO.output(init.motor_A_B, GPIO.HIGH)
    GPIO.output(init.motor_B_A, GPIO.HIGH)
    GPIO.output(init.motor_B_B, GPIO.LOW)
    GPIO.output(init.motor_C_A, GPIO.HIGH)
    GPIO.output(init.motor_C_B, GPIO.LOW)
    GPIO.output(init.motor_D_A, GPIO.LOW)
    GPIO.output(init.motor_D_B, GPIO.HIGH)

def car_turn_left():                        #小车向左旋转
    GPIO.output(init.motor_A_A, GPIO.HIGH)
    GPIO.output(init.motor_A_B, GPIO.LOW)
    GPIO.output(init.motor_B_A, GPIO.HIGH)
    GPIO.output(init.motor_B_B, GPIO.LOW)
    GPIO.output(init.motor_C_A, GPIO.HIGH)
    GPIO.output(init.motor_C_B, GPIO.LOW)
    GPIO.output(init.motor_D_A, GPIO.HIGH)
    GPIO.output(init.motor_D_B, GPIO.LOW)

def car_turn_right():                        #小车向右旋转
    GPIO.output(init.motor_A_A, GPIO.LOW)
    GPIO.output(init.motor_A_B, GPIO.HIGH)
    GPIO.output(init.motor_B_A, GPIO.LOW)
    GPIO.output(init.motor_B_B, GPIO.HIGH)
    GPIO.output(init.motor_C_A, GPIO.LOW)
    GPIO.output(init.motor_C_B, GPIO.HIGH)
    GPIO.output(init.motor_D_A, GPIO.LOW)
    GPIO.output(init.motor_D_B, GPIO.HIGH)

def car_left_parallel():                        #小车向左平移
    GPIO.output(init.motor_A_A, GPIO.LOW)
    GPIO.output(init.motor_A_B, GPIO.HIGH)
    GPIO.output(init.motor_B_A, GPIO.LOW)
    GPIO.output(init.motor_B_B, GPIO.HIGH)
    GPIO.output(init.motor_C_A, GPIO.HIGH)
    GPIO.output(init.motor_C_B, GPIO.LOW)
    GPIO.output(init.motor_D_A, GPIO.HIGH)
    GPIO.output(init.motor_D_B, GPIO.LOW)

def car_right_parallel():                        #小车向右平移
    GPIO.output(init.motor_A_A, GPIO.HIGH)
    GPIO.output(init.motor_A_B, GPIO.LOW)
    GPIO.output(init.motor_B_A, GPIO.HIGH)
    GPIO.output(init.motor_B_B, GPIO.LOW)
    GPIO.output(init.motor_C_A, GPIO.LOW)
    GPIO.output(init.motor_C_B, GPIO.HIGH)
    GPIO.output(init.motor_D_A, GPIO.LOW)
    GPIO.output(init.motor_D_B, GPIO.HIGH)

def car_stop():                                 #小车停止
    GPIO.output(init.motor_A_A, GPIO.LOW)
    GPIO.output(init.motor_A_B, GPIO.LOW)
    GPIO.output(init.motor_B_A, GPIO.LOW)
    GPIO.output(init.motor_B_B, GPIO.LOW)
    GPIO.output(init.motor_C_A, GPIO.LOW)
    GPIO.output(init.motor_C_B, GPIO.LOW)
    GPIO.output(init.motor_D_A, GPIO.LOW)
    GPIO.output(init.motor_D_B, GPIO.LOW)