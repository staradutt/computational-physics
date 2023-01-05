import numpy as np 
from matplotlib import pyplot as plt 
ht=0.1

g=9.8
M=(g*ht**2)

t_arr=np.arange(0,10+0.5*ht,ht)
x_arr=[0. for t in t_arr]


error=100

while error>1e-6:
	xcopy=np.copy(x_arr)
	for i in range(1,len(x_arr)-1):
		x_arr[i]=0.5*(x_arr[i+1]+x_arr[i-1]+M)
	
	error=np.max(abs(x_arr-xcopy))
	
	
plt.plot(t_arr,x_arr)
plt.xlabel('t (s)')
plt.ylabel('x (m)')
plt.savefig('trajectory.png')
plt.clf()