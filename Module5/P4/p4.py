import numpy as np 
from matplotlib import pyplot as plt 
#function for harmonic oscillator
def f1(x):
	return np.array([x[1] , -omega**2 * x[0]])
#function for part anharmonic oscillator
def f2(x):
	return np.array([x[1] , -omega**2 * (x[0]**3)])
#function for van der pol
def f3(x):
	return np.array([ x[1] , mu*(1-x[0]**2)*x[1] - (omega**2 * x[0]) ])

def RK4(ts,tf,N,xinitial,f):
	h=(tf-ts)/N
	t_arr=np.arange(ts,tf,h)
	x_arr=[]
	y_arr=[]#y=dx/dt
	x=xinitial
	for t in t_arr:
		x_arr.append(x[0])
		y_arr.append(x[1])
	
		k1=f(x)*h
		k2=h*f(x+0.5*k1)
		k3=h*f(x+0.5*k2)
		k4=h*f(x+k3)
		x+=(k1+2*k2+2*k3+k4)/6
	return t_arr,x_arr,y_arr
omega=1
#part a 
t_array11,x_array11,y_array11=RK4(0,50,1000,[1,0],f1)
plt.plot(t_array11,x_array11,label='initial x = 1')
#part b 
t_array1,x_array1,y_array1=RK4(0,50,1000,[2,0],f1)
plt.plot(t_array1,x_array1,label='initial x = 2')

plt.legend()
plt.title('x\'\'=-(w^2)*x where, w = 1,initial x\' = 0')
plt.savefig('harmonic.png')
plt.clf()


#part c
t_array21,x_array21,y_array21=RK4(0,50,1000,[1,0],f2)
plt.plot(t_array21,x_array21,label='initial x = 1')
t_array2,x_array2,y_array2=RK4(0,50,1000,[2,0],f2)
plt.plot(t_array2,x_array2,label='initial x = 2')
plt.legend()
plt.title('x\'\'=-(w^2)*(x^3) where, w = 1,initial x\' = 0')
plt.savefig('anharmonic.png')
plt.clf()
#part d
plt.plot(x_array11,y_array11,label='harmonic')
plt.plot(x_array21,y_array21,label='anharmonic')
plt.axis('equal')
plt.legend()
plt.title('phase space plot')
plt.savefig('part_d')
plt.clf()
#part e
mu=1.0
t_array3,x_array3,y_array3=RK4(0,20,10000,[1,0],f3)
plt.plot(x_array3,y_array3,label='vdp, mu = 1')
mu=2
t_array3,x_array3,y_array3=RK4(0,50,10000,[1,0],f3)
plt.plot(x_array3,y_array3,label='vdp, mu = 2')
mu=4
t_array3,x_array3,y_array3=RK4(0,50,10000,[1,0],f3)
plt.plot(x_array3,y_array3,label='vdp, mu = 4')

plt.legend()
plt.title('phase space plot for \n van der pol oscillator' )
plt.savefig('van_der_pol.png')

plt.plot(x_array11,y_array11,label='harmonic')
plt.plot(x_array21,y_array21,label='anharmonic')
plt.axis('equal')
plt.legend()
plt.title('phase space plot')
plt.savefig('combined_phase_space_plot.png')
plt.clf()