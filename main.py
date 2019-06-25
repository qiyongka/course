#!/usr/bin/env python2
# -*- coding: utf-8 -*-

'''
from __future__ import division
import cv2
import time
import numpy as np

def capture():
    global x, y
    ret,frame=cap.read()

    frame=cv2.GaussianBlur(frame,(5,5),0)                    #高斯模糊
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)                #转hsv
    mask=cv2.inRange(hsv,yellow_lower,yellow_upper)          #生成掩膜
    
    #形态学操作
    mask=cv2.erode(mask,None,iterations=2)
    mask=cv2.dilate(mask,None,iterations=2)
    mask=cv2.GaussianBlur(mask,(3,3),0)
    res=cv2.bitwise_and(frame,frame,mask=mask)               #与运算
    cnts=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,
                          cv2.CHAIN_APPROX_SIMPLE)[-2]       #检测颜色的轮廓
    if len(cnts)>0:
        cnt = max (cnts,key=cv2.contourArea)
        (x,y),radius=cv2.minEnclosingCircle(cnt)
        cv2.circle(frame,(int(x),int(y)),int(radius)*2,
                   (255,0,255),2)                            #找到后在每个轮廓上画圆
    else:
        x=0
        y=0   
    cv2.imshow('capture',frame)
    if cv2.waitKey(1)==119:
        exit()

########################################################
cap=cv2.VideoCapture(0)

#设置摄像头分辨率为（640，480）
#如果感觉图像卡顿严重，可以降低为（320，240）
cap.set(3,640)
cap.set(4,480)

#设置黄色的阙值 使用HSV空间
yellow_lower=np.array([156,43,46])
yellow_upper=np.array([180,255,255])

time.sleep(1)
x=0
y=0
while 1:
    #ret为是否找到图像， frame是帧本身
    capture()
    print('x:',x,'y:',y)
    if(x == 0 and y == 0): # can not get the target
        #旋转
        time.sleep(1)
        continue
    if (x!=0 or y!=0 ):
        #car.stop()
        if(x > 320):
            print('right---start')
            time.sleep(1)
        else:
            print('left---start')
            time.sleep(1)
    

    
cap.release()
cv2.destroyAllWindows()
'''

'''

此次修改后，该文件为总控文件
Author： Zhang Jianxin


'''



import color_capture
import time

stop_tag = 0
#停止标志
obstacle_tag = 0
#障碍物标志

while 1:
	#检测是否停止
	#code here
	if stop_tag==1:
		#车子停下来
		#摄像头寻找目标，直至找到为止
		#code here 
	elif stop_tag==0:
		#车子在动
		#检测障碍物
		if obstacle_tag==0:
			#没有障碍物，进入正常寻迹捕捉模式
			#检测识别目标位置
			#做出改变
		elif obstacle_tag==1:
			#进入避障程序
			#code here
