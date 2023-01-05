import numpy as np
from matplotlib import pyplot as plt

sig=10
r=28
bi=8/3

def f(x):
	return np.asarray([sig*(x[1]-x[0]) , r*x[0] - x[1] - x[0]*x[2] , x[0]*x[1] - bi*x[2]])



a=0
b=50.0
N=20000
h=(b-a)/N
t_arr=np.arange(a,b,h)
x_arr=[]
y_arr=[]
z_arr=[]
x=[0.0,1.0,0.0]
for t in t_arr:
	x_arr.append(x[0])
	y_arr.append(x[1])
	z_arr.append(x[2])
	k1=f(x)*h
	k2=h*f(x+0.5*k1)
	k3=h*f(x+0.5*k2)
	k4=h*f(x+k3)
	x+=(k1+2*k2+2*k3+k4)/6
plt.figure(figsize=(10,5))
plt.plot(t_arr,y_arr)
plt.savefig('y_vs_t.png')
plt.clf()
plt.plot(x_arr,z_arr)
plt.savefig('strng_attr.png')
plt.clf()
