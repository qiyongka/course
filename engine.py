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
        print("speed" + s)


# test
'''
car = Engine(11, 12, 13, 15, 16)
while 1:
    car.start(speed)
    time.sleep(3)
    car.stop()
    time.sleep(3)
    car.back(50)
    time.sleep(3)
    car.start(speed)
    car.change_speed(65)
    time.sleep(3)
    car.forward_left_single(speed)
    time.sleep(1)
    car.forward_right_single(speed)
    time.sleep(1)
    car.back_left_single(speed)
    time.sleep(1)
    car.back_right_single(speed)
    time.sleep(1)
    car.left_double(speed)
    time.sleep(1)
    car.right_double(speed)
    break
'''



