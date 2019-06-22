# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
servoPin = 24
GPIO.setup(servoPin, GPIO.OUT)

class Servo1:
    servoPin = 24

    def __init__(self, a):
        self.servoPin = a

    def servo_pulse(self , myangle):
        pulsewidth = (myangle * 11) + 500
        GPIO.output(self.servoPin, GPIO.HIGH)
        time.sleep(pulsewidth/1000000.0)
        GPIO.output(servoPin, GPIO.LOW)
        time.sleep(20.0/1000-pulsewidth/1000000.0)

    def servo_control_forward(self,angle) :
        for pos in range(angle):
            self.servo_pulse(pos)
            time.sleep(0.009) 

    def servo_control_reserve(self,angle) :
        for pos in reversed(range(angle)):                                                                  
            self.servo_pulse(pos)
            time.sleep(0.009)
'''
steer1 = Servo1(24)
while 1:
    steer.servo_control_forward(100)
    time.sleep(3)
    steer.servo_control_reserve(100)
    time.sleep(3)
    GPIO.cleanup()
    break
'''