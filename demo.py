import sys
import wifi
import pywifi
import sympy
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.pyplot import plot
from matplotlib.pyplot import show


global rssi1
global rssi2
global rssi3
rssi1 = 0
rssi2 = 0
rssi3 = 0

def triposition(xa,ya,da,xb,yb,db,xc,yc,dc):
    x,y=sympy.symbols('x y')

    f1 = 2*x*(xa-xc)+np.square(xc)-np.square(xa)+2*y*(ya-yc)+np.square(yc)-np.square(ya)-(np.square(dc)-np.square(da))

    f2 = 2*x*(xb-xc)+np.square(xc)-np.square(xb)+2*y*(yb-yc)+np.square(yc)-np.square(yb)-(np.square(dc)-np.square(db))

    result = sympy.solve([f1,f2],[x,y])
    locx,locy = result[x],result[y]
    return [locx,locy]

def rssi_get() :
    global rssi1
    global rssi2
    global rssi3
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    # 起始获得的是列表，列表中存放的是无线网卡对象。
    # 可能一台电脑有多个网卡，请注意选择


    # 如果网卡选择错了，程序会卡住，不出结果。
    iface.scan()

    result=iface.scan_results()

    for i in range(len(result)):
        if result[i].ssid == "Public1" :
            print('signal level:',result[i].ssid, result[i].signal)
            rssi1 = result[i].signal
        if result[i].ssid == "Public2" :
            print('signal level:',result[i].ssid, result[i].signal) 
            rssi2 = result[i].signal
        if result[i].ssid == "Public3" :
            print('signal level:',result[i].ssid, result[i].signal)  
            rssi3 = result[i].signal 
        #ssid 是名称 ，signal 是信号强度


rssi_get()

d1 = 0.00018 * rssi1 * rssi1 * rssi1 + 0.066 * rssi1 * rssi1 + 0.8 * rssi1 + 0.12

d2 = 0.00018 * rssi2 * rssi2 * rssi2 + 0.066 * rssi2 * rssi2 + 0.8 * rssi2 + 0.12

d3 = 0.00018 * rssi3 * rssi3 * rssi3 + 0.066 * rssi3 * rssi3 + 0.8 * rssi3 + 0.12


print ('node one distance: ', d1)

print ('node two distance: ', d2)

print ('node three distance:',d3)

(m,n)=triposition(100,0,d1,0,100,d2,200,0,d3)

print ('position:',m,'cm',n,'cm')
