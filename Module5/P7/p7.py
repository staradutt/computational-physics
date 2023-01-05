import numpy as np 
from matplotlib import pyplot as plt 
from math import cos 


def RK4(start,stop,Nt,N):
	
	def f(x,t):
	
		omega=2
		k=6
		arr=[]
		for i in range(N):
			arr.append(x[i+N])
		arr.append(k*(x[1]-x[0])+cos(omega*t))
		for i in range(2,N):
			arr.append(k*(x[i]-2*x[i-1]+x[i-2]))
		arr.append(k*(x[N-2]-x[N-1]))
		return np.array(arr)


	x=np.zeros(2*N)
	h=(stop-start)/Nt
	t_arr=np.arange(start,stop,h)
	data=[[] for r in range(N)]
	
	for t in t_arr:
		for i in range(N):
			data[i].append(x[i])
		k1=h*f(x,t)
		k2=h*f(x+0.5*k1,t+0.5*h)
		k3=h*f(x+0.5*k2,t+0.5*h)
		k4=h*f(x+k3,t+h)
		x+=(k1+2*k2+2*k3+k4)/6
	
	for i in range(N):
		plt.plot(t_arr,data[i],label='i = '+str(i))
	
	plt.legend()
	plt.xlabel('t')
	plt.title('N = '+str(N))
	plt.savefig('N_'+str(N))

RK4(0,20,1000,5)





#for t in t_arr:


