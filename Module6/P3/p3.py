import numpy as np 
from matplotlib import pyplot as plt 
from math import e,exp


hx=0.01
ht=1e-6
v=100
M=(v/hx)**2*ht
C=1
sigma=0.3
L=1
d=0.1
def u_initial(x):
	return C*(x/L)*((L-x)/L)*exp(-0.5*((x-d)/sigma)**2)








x_arr=np.arange(0,1+0.5*hx,hx)
z_arr=[0. for x in x_arr]
u_arr=[u_initial(x) for x in x_arr]
t_arr=[]
start=0
stop=1e-1
t=start
count=0
cnt2=0

while t<stop:
	t_arr.append(t)
	zcopy=np.copy(z_arr)
	ucopy=np.copy(u_arr)
	for i in range(1,len(x_arr)-1):

		z_arr[i]=zcopy[i]+ucopy[i]*ht
		u_arr[i]=ucopy[i]+M*(zcopy[i+1]-2*zcopy[i]+zcopy[i-1])
	count+=1
	
	if count in [k*1e3 for k in (range(100))]:
					
					plt.plot(x_arr,z_arr,linewidth=4)
					plt.ylim(-0.0005,0.0005)
					
					plt.title('t = '+str(round(t,3))+' s')
					plt.savefig('vib'+str(cnt2)+'.png')
					plt.clf()
					cnt2+=1
			
	t+=ht

