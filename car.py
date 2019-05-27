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

    def start(self, s):
        pwma.ChangeDutyCycle(s)
        GPIO.output(self.INT1, GPIO.HIGH)
        GPIO.output(self.INT2, GPIO.LOW)
        GPIO.output(self.INT3, GPIO.HIGH)
        GPIO.output(self.INT4, GPIO.LOW)
        print("start")

    def stop(self):
        GPIO.output(self.INT1, GPIO.LOW)
        GPIO.output(self.INT2, GPIO.LOW)
        GPIO.output(self.INT3, GPIO.LOW)
        GPIO.output(self.INT4, GPIO.LOW)
        print("stop")

    def back(self, s):
        pwma.ChangeDutyCycle(s)
        GPIO.output(self.INT1, GPIO.LOW)
        GPIO.output(self.INT2, GPIO.HIGH)
        GPIO.output(self.INT3, GPIO.LOW)
        GPIO.output(self.INT4, GPIO.HIGH)
        print("back")

    def forward_left_single(self, s):
        pwma.ChangeDutyCycle(s)
        GPIO.output(self.INT1, GPIO.LOW)
        GPIO.output(self.INT2, GPIO.LOW)
        GPIO.output(self.INT3, GPIO.HIGH)
        GPIO.output(self.INT4, GPIO.LOW)
        print("fls")

    def forward_right_single(self, s):
        pwma.ChangeDutyCycle(s)
        GPIO.output(self.INT1, GPIO.HIGH)
        GPIO.output(self.INT2, GPIO.LOW)
        GPIO.output(self.INT3, GPIO.LOW)
        GPIO.output(self.INT4, GPIO.LOW)
        print("frs")

    def back_left_single(self, s):
        pwma.ChangeDutyCycle(s)
        GPIO.output(self.INT1, GPIO.LOW)
        GPIO.output(self.INT2, GPIO.LOW)
        GPIO.output(self.INT3, GPIO.LOW)
        GPIO.output(self.INT4, GPIO.HIGH)
        print("bls")

    def back_right_single(self, s):
        pwma.ChangeDutyCycle(s)
        GPIO.output(self.INT1, GPIO.LOW)
        GPIO.output(self.INT2, GPIO.HIGH)
        GPIO.output(self.INT3, GPIO.LOW)
        GPIO.output(self.INT4, GPIO.LOW)
        print("brs")

    def left_double(self, s):
        pwma.ChangeDutyCycle(s)
        GPIO.output(self.INT1, GPIO.LOW)
        GPIO.output(self.INT2, GPIO.HIGH)
        GPIO.output(self.INT3, GPIO.HIGH)
        GPIO.output(self.INT4, GPIO.LOW)
        print("ld")

    def right_double(self, s):
        pwma.ChangeDutyCycle(s)
        GPIO.output(self.INT1, GPIO.HIGH)
        GPIO.output(self.INT2, GPIO.LOW)
        GPIO.output(self.INT3, GPIO.LOW)
        GPIO.output(self.INT4, GPIO.HIGH)
        print("rd")

    def change_speed(self, s):
        pwma.ChangeDutyCycle(s)
        print("speed")


# test
car = Engine(11, 12, 13, 15, 16)
while 1:
    car.start(speed)# 启动前进，speed为默认速度90，其中输入的速度值在0到100，不能溢出
    time.sleep(3)
    car.stop()# 停止
    time.sleep(3)
    car.back(50)# 后退
    time.sleep(3)
    car.start(speed)
    car.change_speed(15)# 变速
    time.sleep(3)
    car.forward_left_single(speed)# 单轮向前左转
    time.sleep(1)
    car.forward_right_single(50)# 单轮向前右转
    time.sleep(1)
    car.back_left_single(speed)# 单轮向后左转
    time.sleep(1)
    car.back_right_single(5)# 单轮向后右转
    time.sleep(1)
    car.left_double(speed)# 原地左转
    time.sleep(1)
    car.right_double(30)# 原地右转
    GPIO.cleanup()
    break




