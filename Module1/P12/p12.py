import numpy as np
from matplotlib import pyplot as plt
from math import sin,cos,pi,e

#number of sample points in theta arrays
N=1000
#part a>>  'deltoid'
#creating theta array

theta_vals=np.linspace(0,2*pi,N)
#creating x,y arrays
x1=[]
y1=[]
for i in theta_vals:
	x1.append(2*cos(i)+cos(2*i))
	y1.append(2*sin(i)-sin(2*i))
#plotting
plt.plot(x1,y1)
plt.savefig('a')
plt.clf()

#part b>>  'galilean spiral'
#creating theta array
theta_vals2=np.linspace(0,10*pi,N)
#creating x,y arrays
x2=[]
y2=[]
for val in theta_vals2:
	x2.append((val**2) * cos(val))
	y2.append((val**2) * sin(val))
#plotting
plt.plot(x2,y2)
plt.savefig('b')
plt.clf()

#part c>>  'feys'
#creating theta array
theta_vals3=np.linspace(0,24*pi,10*N)
#creating x,y arrays
x3=[]
y3=[]
def feys(t):
	return((e**cos(t))-2*cos(4*t)+((sin(t/12))**5))

for val in theta_vals3:
	x3.append(feys(val)*cos(val))
	y3.append(feys(val)*sin(val))
#plotting
plt.plot(x3,y3)
plt.savefig('c')
plt.clf()



