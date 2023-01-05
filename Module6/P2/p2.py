import numpy as np 
from matplotlib import pyplot as plt 
from math import pi,sin
tao=365
A=10
B=12

def t_ini(t):
	return A+B*sin(2*pi*t/(tao)) 

D=0.1
hd=0.1
ht=0.05
M=D*ht/(hd)**2

t_arr=np.arange(0,9*365+0.5*ht,ht)
x_arr=np.arange(0,20+0.5*hd,hd)
temp_x=[10.0 for x in x_arr]
temp_x[len(temp_x)-1]=11
temp_x[0]=t_ini(0)
#temp x initial is all set 
for i in range(len(t_arr)):
	tcopy=np.copy(temp_x)#copy of temp values from previous time 
	#construction of temp values in new time
	temp_x[0]=t_ini(t_arr[i])
	
	for j in range(1,len(temp_x)-1):
		temp_x[j]=tcopy[j]*(1-2*M)+M*(tcopy[j+1]+tcopy[j-1])
print('9 yr simulation done')


for k in range(4):
	t_arr=np.arange((9+k*0.25)*365,(9+(k+1)*0.25)*365,ht)
	


	for i in range(len(t_arr)):
		tcopy=np.copy(temp_x)#copy of temp values from previous time 
		#construction of temp values in new time
		temp_x[0]=t_ini(t_arr[i])
		
		for j in range(1,len(temp_x)-1):
			temp_x[j]=tcopy[j]*(1-2*M)+M*(tcopy[j+1]+tcopy[j-1])
		
	
	plt.plot(x_arr,temp_x,label='quarter '+str(k+1))
	
	print('quarter '+str(k)+' calculation done.')
print('complete')
plt.legend()
plt.xlabel('Depth (m)')
plt.ylabel('Temp (\u00B0C)')
plt.savefig('Temp_profile.png')


