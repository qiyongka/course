# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

#ͳһ����gpio�����ӿڷ�ʽ

Trig_Pin = 19
Echo_Pin = 21


GPIO.setup(Trig_Pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(Echo_Pin, GPIO.IN)

class Sound1:
    Trig_Pin = 19
    Echo_Pin = 21

    def __init__(self, f, g):
	self.Trig_Pin = f
	self.Echo_Pin = g

    def checkdist(self):
	GPIO.output(self.Trig_Pin, GPIO.HIGH)
	time.sleep(0.00015)
	GPIO.output(self.Trig_Pin, GPIO.LOW)
	while not GPIO.input(self.Echo_Pin):
	    pass
	t1 = time.time()
	while GPIO.input(self.Echo_Pin):
	    pass
	t2 = time.time()
	return (t2-t1)*340*100/2
