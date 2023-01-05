import numpy as np 
from matplotlib import pyplot as plt 
from math import sqrt 


G=1
M=10
L=2
def f(x):
	r2=x[0]**2 + x[1]**2
	k=-G*M/(r2*sqrt(r2+0.25*L**2))
	return np.array([ x[2], x[3], k*x[0], k*x[1] ])

x=[1.0,0.0,0.0,1.0]
N=1000
h=10/N
t_arr=np.arange(0,10,h)
x_arr=[]
y_arr=[]
for t in t_arr:
	x_arr.append(x[0])
	y_arr.append(x[1])

	k1=h*f(x)
	k2=h*f(x+0.5*k1)
	k3=h*f(x+0.5*k2)
	k4=h*f(x+k3)
	x+=(k1+2*k2+2*k3+k4)/6
plt.plot(x_arr,y_arr,'lightcoral')
plt.title('trajectory')
plt.savefig('trajectory.png')
plt.clf()