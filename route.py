import numpy as np
import math

new=['A','B','C']
old = ['A','B']
A=[99,1]
B=[1,2]
C=[2,5]
D=[5,5]

x=0
y=0

def angle_cacaulate(x_now,y_now,x_1,y_1):
	pi =3.1415926

	d = math.sqrt((x_now - x_1) * (x_now - x_1) + (x_now - x_1) * (x_now - x_1))

	m = math.atan2((y_1 - y_now),(x_1 - x_now))   /pi *180 +180

	theta = int(m)

	return theta

def distance(p1 = [], p2 = []):
	p1=np.array(p1)
	p2=np.array(p2)
	p3=p2-p1
	p4=math.hypot(p3[0],p3[1])
	return p4


def route(new_array=[],A=[],B=[],C=[],D=[]):
	'''
	new 新节点信息 old 旧节点信息，A，B，C，D 是待充电节点坐标
	'''

	global x,y	#车子当前节点
	pos = []
	dist = []
	for i in range(0,4):
		pos.append([999,999])
	#决定去哪个节点充电
	print(pos)
	for i in range(0,len(new_array)):
		#节点坐标转换
		if new_array[i] is 'A':
			pos[0] = A
		elif new_array[i] is 'B':
			pos[1] = B
		elif new_array[i] is 'C':
			pos[2] = C
		elif new_array[i] is 'D':
			pos[3] = D
	#计算距离最小值
	for j in range(0,len(pos)):
		dis = distance([x,y],pos[j])
		dist.append(dis)

	mi = min(dist) 
	p = dist.index(mi)

	print(dist)
	print(dis)
	print(mi)

	angle = angle_cacaulate(x,y,pos[p][0],pos[p][1])

	return angle

print(route(new,A,B,C,D))

