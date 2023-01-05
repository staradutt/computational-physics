import numpy as np 
from matplotlib import pyplot as plt 

M=1.989e30
G=6.67408e-11
m=5.9722e24

def f(x):
	r=np.sqrt(x[0]**2+x[1]**2)
	return np.array([ x[2], x[3], -G*M*x[0]/r**3, -G*M*x[1]/r**3 ])

def verlet(xinitial, start, stop,h):
	x_arr=[]
	y_arr=[]
	v_arr=[]
	t_arr=[]

	x=np.copy(xinitial)
	v=x+0.5*h*f(x)
	t=start
	while t<stop:
		x=x+h*f(v)
		k=h*f(x)
		v=v+0.5*k
		x_arr.append(x[0])
		y_arr.append(x[1])
		v_arr.append((v[2]**2+v[3]**2)**0.5)
		t_arr.append(t)
		v=v+0.5*k
		t+=h
	return x_arr,y_arr,v_arr,t_arr
x_arr,y_arr,v_arr,t_arr=verlet([1.471e11, 0, 0, 3.0287e4], 0, 3 * 365 * 24 * 3600, 3600)

PE_arr=[-G*M*m / ((x_arr[i]**2+y_arr[i]**2)**0.5) for i in range(len(x_arr)) ]
KE_arr=[0.5*m*v**2 for v in v_arr]

plt.plot(x_arr,y_arr)
plt.xlabel('x')
plt.ylabel('y')
plt.title('trajectory')
plt.savefig('trajectory.png')
plt.clf()

plt.plot(t_arr,PE_arr,label='PE')
plt.plot(t_arr,KE_arr,label='KE')
plt.plot(t_arr,np.array(PE_arr)+np.array(KE_arr),label='KE+PE')
plt.legend()
plt.savefig('energy_plots.png')
plt.clf()

plt.plot(t_arr,np.array(PE_arr)+np.array(KE_arr),label='Total Energy')
plt.legend()
plt.savefig('total_Energy.png')
plt.clf()
