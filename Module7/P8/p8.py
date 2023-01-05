import random
import numpy as np 
from numpy import e,pi,log,cos
from matplotlib import pyplot as plt

def func1(x):
	return x**2-cos(4*pi*x)

def func2(x):
	if x>=0 and x<=50:
		return cos(x)+cos((2**0.5)*x)+cos((3**0.5)*x)
	else:
		return float('inf')

def cooling_schd(t):
	a=0.9999
	return a*t

def gs_rnd():
	z=random.random()
	tht=2*pi*random.random()
	r=(-2*log(1 - z))**0.5
	return r*cos(tht)


def sim_annealing(initial,f):
	x=initial
	T=1
	t = 0
	tmin=1e-10
	x_arr=[]
	t_arr=[]
	while T>tmin:
		delta=gs_rnd()
		if f(x+delta)<f(x):
			x+=delta
		else:
			p=e**(-(f(x+delta)-f(x))/T)
			

			if random.random()<p:
				
				x += delta
		T=cooling_schd(T)
		x_arr.append(x)
		t_arr.append(t)
		t += 1
	plt.plot(t_arr, x_arr, ".")
	return x

min1=sim_annealing(2,func1)
plt.savefig('plot1.png')
plt.close()
print('minima for function1 = ',round(min1,3))

min1=sim_annealing(8,func2)
plt.savefig('plot2.png')
plt.close()
print('minima for function2 = ',round(min1,3))
