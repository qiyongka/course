# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
#统一成用gpio物理接口方式

Trig_Pin = 18
Echo_Pin = 22


GPIO.setup(Trig_Pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(Echo_Pin, GPIO.IN)

time.sleep(2)

def checkdist():
	GPIO.output(Trig_Pin, GPIO.HIGH)
	time.sleep(0.00015)
	GPIO.output(Trig_Pin, GPIO.LOW)
	while not GPIO.input(Echo_Pin):
		pass
	t1 = time.time()
	while GPIO.input(Echo_Pin):
		pass
	t2 = time.time()
	return (t2-t1)*340*100/2

try:
	while True:
		print 'Distance:%0.2f cm' % checkdist()
	 	time.sleep(1)
except KeyboardInterrupt:			#ctrl+c	finish 
	GPIO.cleanup()
