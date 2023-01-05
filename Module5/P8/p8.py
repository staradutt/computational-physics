import numpy as np 
from matplotlib import pyplot as plt 
from math import sqrt

M=1.989e30
G=6.67408e-11
def f(x):
	r=sqrt(x[0]**2+x[1]**2)
	return np.array([ x[2], x[3], -(G*M*x[0])/r**3, -(G*M*x[1])/r**3 ])
def rk4(xinitial, start, stop, h):
	x_arr=[]
	y_arr=[]
	t=start
	x=xinitial
	while t<stop:
		x_arr.append(x[0])
		y_arr.append(x[1])
		
		k1=h*f(x)
		k2=h*f(x+k1/2)
		k3=h*f(x+k2/2)
		k4=h*f(x+k3)
		x+=(k1+2*k2+2*k3+k4)/6 
		t+=h
	return x_arr,y_arr,x

tp=49*365*24*3600
x_arr,y_arr,x2start=rk4([4e12,0,0,500.0],0,tp,0.00001*tp)
plt.plot(x_arr,y_arr,label='orbit1',linewidth=5)
x_arr,y_arr,x2start=rk4(x2start,0,tp,0.00001*tp)
plt.plot(x_arr,y_arr,label='orbit2')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('trajectory_normal.png')
plt.clf()

def adptRK4(xinitial,start,stop,hin):
	delta=1000/(365*24*3600)
	x_arr=[]
	y_arr=[]
	t=start
	x=xinitial
	h=hin
	maxh=10*h
	
	while t<stop:
		xcopy=np.copy(x)
		x_arr.append(x[0])
		y_arr.append(x[1])
		for i in range(2):
			k1=h*f(x)
			k2=h*f(x+0.5*k1)
			k3=h*f(x+0.5*k2)
			k4=h*f(x+k3)
			x+=(k1+2*k2+2*k3+k4)/6
			t+=h
		xtplus2h_est1=x
		
		k1=2*h*f(xcopy)
		k2=2*h*f(xcopy+0.5*k1)
		k3=2*h*f(xcopy+0.5*k2)
		k4=2*h*f(xcopy+k3)
		xtplus2h_est2=xcopy+(k1+2*k2+2*k3+k4)/6
		

		diff=sqrt( (xtplus2h_est2[0]-xtplus2h_est1[0])**2 + (xtplus2h_est2[1]-xtplus2h_est1[1])**2 ) 
		
		h*=((30*h*delta)/(diff))**0.25
		if h>=maxh:
			h=maxh
	return x_arr,y_arr
x_arr,y_arr=adptRK4([4e12,0,0,500.0],0,tp,0.001* tp)	
plt.scatter(x_arr,y_arr,marker='.')
plt.title('adaptiveRK4')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('adaptiveRK4.png')
plt.clf()






