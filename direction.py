import math
#import HMC5883L
def angle_cacaulate(X_now,y_now,X_1,y_1): 
	pi =3.1415926

	d = math.sqrt((x_now - x_1) * (x_now - x_1) + (x_now - x_1) * (x_now - x_1))

	m = math.atan2((y_1 - y_now),(x_1 - x_now))   /pi *180 +180

	theta = int(m)
	return theta
