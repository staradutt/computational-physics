import numpy as np 
from math import sqrt,pi
from matplotlib import pyplot as plt 


grav=9.8
def k_bi_m(mass):
	rho=1.22
	C=0.47
	return pi*0.08**2 *rho*C*(1/mass)

def f(x):
	return np.array([ x[2] , x[3] , -(k)*x[2]*sqrt(x[2]**2 + x[3]**2) , -grav - (k)*x[3]*sqrt(x[2]**2 + x[3]**2) ])
def RK4(ts,tf,N):
	h=(tf-ts)/N
	x=[0,0,50*3**0.5,50]
	t_arr=np.arange(ts,tf,h)
	x_arr=[]
	y_arr=[]
	vx_arr=[]
	vy_arr=[]

	for t in t_arr:
		if x[1]<0:
			break
		x_arr.append(x[0])
		y_arr.append(x[1])
		vx_arr.append(x[2])
		vy_arr.append(x[3])
		k1=h*f(x)
		k2=h*f(x+0.5*k1)
		k3=h*f(x+0.5*k2)
		k4=h*f(x+k3)
		x+=(k1+2*k2+2*k3+k4)/6
	return np.array([t_arr,x_arr,y_arr,vx_arr,vy_arr])
def dist_trav(x_arr,y_arr):
	d=0
	for i in range(len(x_arr)-1):
		d+=sqrt((x_arr[i+1]-x_arr[i])**2+(y_arr[i+1]-y_arr[i])**2)
	return d	




mass_arr=[0.1, 1, 10, 50, 100, 500, 1000]
dist_arr=[]
for i in mass_arr:
	k=k_bi_m(i)
	data=RK4(0,30,1000)
	plt.plot(data[1],data[2],label='m='+str(i))
	dist_arr.append(dist_trav(data[1],data[2]))
k=0
data=RK4(0,30,1000)
plt.plot(data[1],data[2],label='no air res')
distlim=dist_trav(data[1],data[2])
plt.xlim(-10,900)
plt.ylim(-10,200)
plt.legend()
plt.title('trajectories')
plt.savefig('trajectories.png')
plt.clf()

plt.scatter(mass_arr,dist_arr)
plt.axhline(y=distlim,color='r',label='no air res,'+str(round(distlim,2))+'m')
plt.legend()
plt.xlabel('mass of cannon (in kg)')
plt.ylabel('distance travelled over the ground (in m)')
plt.title('distance vs mass')
plt.savefig('dist_vs_m.png')
plt.clf()

