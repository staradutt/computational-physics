import numpy as np 
from matplotlib import pyplot as plt

def vin(t):
	if np.floor(2*t)%2==0:
		return 1
	else:
		return -1


def rk4(start,stop,h,RC):
	
	def f(x,t):
		return (1/RC)*(vin(t)-x)

	t_arr=np.arange(start,stop,h)
	x_arr=[]
	x=0
	for t in t_arr:
		x_arr.append(x)
		k1=h*f(x,t)
		k2=h*f(x+0.5*k1,t+0.5*h)
		k3=h*f(x+0.5*k2,t+0.5*h)
		k4=h*f(x+k3,t+h)
		x+=(k1+2*k2+2*k3+k4)/6
	return t_arr,x_arr
RCaray=[0.01,0.1,1]
for RC in RCaray:
	taray,varay=rk4(0,10,0.01,RC)
	plt.plot(taray,varay,label='RC = '+str(RC))
plt.legend()
plt.ylabel('Vout')
plt.xlabel('t')
plt.savefig('Vout_with_t')	



