# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
INT1 = 11
INT2 = 12
INT3 = 13
INT4 = 15
ENA = 16
GPIO.setup(INT1, GPIO.OUT)
GPIO.setup(INT2, GPIO.OUT)
GPIO.setup(INT3, GPIO.OUT)
GPIO.setup(INT4, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
pwma = GPIO.PWM(16, 80)
pwma.start(90)
speed = 90
default_time = 3


class Engine:
    INT1 = 11
    INT2 = 12
    INT3 = 13
    INT4 = 15
    ENA = 16

    def __init__(self, a, b, c, d, e):
        self.INT1 = a
        self.INT2 = b
        self.INT3 = c
        self.INT4 = d
        self.ENA = e

    def start(self, s, t=None):
        pwma.ChangeDutyCycle(s)
        GPIO.output(self.INT1, GPIO.HIGH)
        GPIO.output(self.INT2, GPIO.LOW)
        GPIO.output(self.INT3, GPIO.HIGH)
        GPIO.output(self.INT4, GPIO.LOW)
        print("start")
        if t is not None:
            time.sleep(t)

    def stop(self, t=None):
        GPIO.output(self.INT1, GPIO.LOW)
        GPIO.output(self.INT2, GPIO.LOW)
        GPIO.output(self.INT3, GPIO.LOW)
        GPIO.output(self.INT4, GPIO.LOW)
        print("stop")
        if t is not None:
            time.sleep(t)

    def back(self, s, t=None):
        pwma.ChangeDutyCycle(s)
        GPIO.output(self.INT1, GPIO.LOW)
        GPIO.output(self.INT2, GPIO.HIGH)
        GPIO.output(self.INT3, GPIO.LOW)
        GPIO.output(self.INT4, GPIO.HIGH)
        print("back")
        if t is not None:
            time.sleep(t)

    def forward_left_single(self, s, t=None):
        pwma.ChangeDutyCycle(s)
        GPIO.output(self.INT1, GPIO.LOW)
        GPIO.output(self.INT2, GPIO.LOW)
        GPIO.output(self.INT3, GPIO.HIGH)
        GPIO.output(self.INT4, GPIO.LOW)
        print("fls")
        if t is not None:
            time.sleep(t)

    def forward_right_single(self, s, t=None):
        pwma.ChangeDutyCycle(s)
        GPIO.output(self.INT1, GPIO.HIGH)
        GPIO.output(self.INT2, GPIO.LOW)
        GPIO.output(self.INT3, GPIO.LOW)
        GPIO.output(self.INT4, GPIO.LOW)
        print("frs")
        if t is not None:
            time.sleep(t)

    def back_left_single(self, s, t=None):
        pwma.ChangeDutyCycle(s)
        GPIO.output(self.INT1, GPIO.LOW)
        GPIO.output(self.INT2, GPIO.LOW)
        GPIO.output(self.INT3, GPIO.LOW)
        GPIO.output(self.INT4, GPIO.HIGH)
        print("bls")
        if t is not None:
            time.sleep(t)

    def back_right_single(self, s, t=None):
        pwma.ChangeDutyCycle(s)
        GPIO.output(self.INT1, GPIO.LOW)
        GPIO.output(self.INT2, GPIO.HIGH)
        GPIO.output(self.INT3, GPIO.LOW)
        GPIO.output(self.INT4, GPIO.LOW)
        print("brs")
        if t is not None:
            time.sleep(t)

    def left_double(self, s, t=None):
        pwma.ChangeDutyCycle(s)
        GPIO.output(self.INT1, GPIO.LOW)
        GPIO.output(self.INT2, GPIO.HIGH)
        GPIO.output(self.INT3, GPIO.HIGH)
        GPIO.output(self.INT4, GPIO.LOW)
        print("ld")
        if t is not None:
            time.sleep(t)

    def right_double(self, s, t=None):
        pwma.ChangeDutyCycle(s)
        GPIO.output(self.INT1, GPIO.HIGH)
        GPIO.output(self.INT2, GPIO.LOW)
        GPIO.output(self.INT3, GPIO.LOW)
        GPIO.output(self.INT4, GPIO.HIGH)
        print("rd")
        if t is not None:
            time.sleep(t)

    def change_speed(self, s, t=None):
        pwma.ChangeDutyCycle(s)
        print("speed")
        if t is not None:
            time.sleep(t)
'''
说明：本代码是电机驱动的类，使用时先把engine对象那个实例化
然后调用各种运动状态改变函数来改变车的运动状态
参数说明：
s ：电机速度，即pwm波占空比，范围是0到100，越大电机速度越快
t ：延时，即该运动状态持续时间，单位：秒
其中stop（）函数只有t参数。
'''

# test

car = Engine(11, 12, 13, 15, 16)
while 1:
    car.start(speed, default_time)
    car.stop(6)
    car.back(50, 5)
    car.start(speed, 1)
    car.change_speed(65, 2)
    car.forward_left_single(speed, 1)
    car.forward_right_single(speed, 2)
    car.back_left_single(speed, 3)
    car.back_right_single(speed, 4)
    car.left_double(speed, 5)
    car.right_double(speed)
    time.sleep(6)
    GPIO.cleanup()
    break




