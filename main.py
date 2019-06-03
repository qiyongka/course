'''
date:2019/6/3
author: zhangjianxin

explainaiton: this code is just a sample file for everyone and it cannot be run. 
			Initialization and event_list haven't been established yet. Hope everybody 
			can put forward more better ideas.
			
'''
import RPi.GPIO as GPIO
import time  


if __name__ == '__main__':
    try:
        #system initialization      
        system_ini()  
        #control the output of volt
        while True:   
            select([dev], [], [])
            for event in  event_list: # if event is in the event list, turn into next, else throw out default  
                if event.code == 103 and event.value == 2:
                    print ("forward")
                    forward() 
                elif event.code == 103 and  event.value == 0: 
                    print("stop forward")
                    stop()
                # above is just a sample
                # I prefer to use  Interrupt vector to define what to do first
                # And we establish a interrrupt vector list apart for convinience

    except(BaseException),e:
        print(e)
        # if default occure, throw out! 
    finally:
        GPIO.cleanup()
        # clean up the system 
