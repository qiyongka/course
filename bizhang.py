# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import sound
import sound1
import engine


if __name__ == "__main__":
    avoid = sound.Sound(18, 22)
    avoid1 = sound1.Sound1(19, 21)
    car = engine.Engine(11, 12, 13, 15, 16)
    
    try:
        while True:
            car.start(40)
	    print 'left:%0.2f cm' % avoid.checkdist()
	    print 'right:%0.2f cm' % avoid1.checkdist()
 	    time.sleep(3)
 	    if avoid.checkdist() < 20 and avoid1.checkdist() < 20 :
                print 'forward have something'
                car.stop()
                car.back(30)
                car.stop()
                car.forward_right_single(30)
                time.sleep(1)
                continue
            if avoid.checkdist() < 20 :
                print 'left have something' 
                car.stop()
                car.forward_right_single(30)
                time.sleep(1)
                continue
            if avoid1.checkdist() < 20 :
                print 'right have somthing'
                car.stop()
                car.forward_left_single(30)
                time.sleep(1)
                continue
            
    except KeyboardInterrupt:			#ctrl+c	finish 
        GPIO.cleanup()
