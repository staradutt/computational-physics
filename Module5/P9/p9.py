import numpy as np 
from matplotlib import pyplot as plt

def f(x):
	return np.array([ x[1], x[1]**2-x[0]-5 ]) 

def leapfrog(xinitial,start,stop,h):
	x_arr=[]
	t_arr=[]
	t=start
	
	x=np.copy(xinitial)
	xmid=x+0.5*h*f(x)
	while t<stop:
		x_arr.append(x[0])
		t_arr.append(t)
		x=x+h*f(xmid)
		xmid=xmid+h*f(x)
		t+=h
	return t_arr,x_arr
t_arr,x_arr=leapfrog([1.0,0.0],0,50,0.001)
plt.plot(t_arr,x_arr)
plt.xlabel('t')
plt.ylabel('x')
plt.savefig('leapfrog.png')
