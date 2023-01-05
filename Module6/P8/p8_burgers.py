import numpy as np 
from matplotlib import pyplot as plt 
from math import sin,pi

def uinit(x):
	return sin(2*pi*x)
def uinit2(x):
	return np.exp(-200*(x-0.3)**2) + np.array([1 if i>=0.6 and i<=0.8 else 0 for i in x])
def Lax2(N,tstop):
	hx=1/N
	x_arr=np.arange(0,1,hx)
	ht=0.5*hx
	f_arr=[uinit(x) for x in x_arr]
	f2_arr=[0.5*u**2 for u in f_arr]
	
	t=0
	
	while t<tstop:
		fcopy=np.copy(f_arr)
		f2copy=np.copy(f2_arr)
		for i in range(-1,N-1):
			f_arr[i]=0.5*(fcopy[i-1]+fcopy[i+1])-ht*(f2copy[i+1]-f2copy[i-1])/(2*hx)
		f2_arr=[0.5*u**2 for u in f_arr]
		t+=ht
	plt.plot(x_arr,f_arr,label=str(tstop))
	
	return x_arr,f_arr,hx

def upwind2(N,tstop):
	hx=1/N
	x_arr=np.arange(0,1,hx)
	ht=0.5*hx
	f_arr=[uinit(x) for x in x_arr]
	f2_arr=[0.5*u**2 for u in f_arr]
	t=0
	
	while t<tstop:
		fcopy=np.copy(f_arr)
		f2copy=np.copy(f2_arr)
		for i in range(-1,N):
			f_arr[i]=fcopy[i]-ht*(f2copy[i]-f2copy[i-1])/hx
		f2_arr=[0.5*u**2 for u in f_arr]
		t+=ht
	plt.plot(x_arr,f_arr,label=str(tstop))
	return x_arr,f_arr,hx

def LW2(N,tstop):
	hx=1/N
	x_arr=np.arange(0,1,hx)
	ht=0.5*hx
	f_arr=[uinit(x) for x in x_arr]
	f2_arr=[0.5*u**2 for u in f_arr]
	t=0
	while t<tstop:
		fcopy=np.copy(f_arr)
		f2copy=np.copy(f2_arr)
		for i in range(-1,N-1):
			m1=0.5*(f2copy[i]+f2copy[i-1])-0.5*ht*(f2copy[i]-f2copy[i-1])/hx
			m2=0.5*(f2copy[i+1]+f2copy[i])-0.5*ht*(f2copy[i+1]-f2copy[i])/hx
			f_arr[i]=fcopy[i]-ht*(m2-m1)/hx
		f2_arr=[0.5*u**2 for u in f_arr]
		t+=ht
	plt.plot(x_arr,f_arr,label=str(tstop))
	return x_arr,f_arr,hx
def lwvisc(uvec,N):
	v=1
	l=0.923*hx
	ucopy=np.zeros(N)
	ucopy1=np.zeros(N)
	

	udup1=np.zeros(N)
	udup2=np.zeros(N)
	
	for j in range(N):
		if uvec[j]<uvec[j-1]:
			ucopy[j]=(uvec[j]-uvec[j-1])/hx
		else:
			ucopy[j]=0.
	temp = l**2*ucopy**2+0.5*uvec**2
	for j in range(-1,N-1):
		udup1[j]=0.5*(uvec[j+1]+uvec[j])-0.5*ht*(temp[j+1]-temp[j])/hx
	for j in range(N):
		if udup1[j]<udup1[j-1]:
			ucopy1[j]=(udup1[j]-udup1[j-1])/hx
		else:
			ucopy1[j]=0.
	temp2 = l**2 * ucopy1**2 + 0.5*udup1**2
	for j in range(N):
		udup2[j]=uvec[j]-ht*(temp2[j]-temp2[j-1])/hx
	return udup2

Lax2(128,0)
Lax2(128,0.1)
Lax2(128,0.25)
Lax2(128,0.5)
plt.title('Lax_burgers')
plt.ylim((-1.5,1.5))

plt.legend()
plt.savefig('Lax_burgers.png')
plt.clf()

upwind2(128,0)
upwind2(128,0.1)
upwind2(128,0.25)
upwind2(128,0.5)
plt.title('upwind_burgers')
plt.ylim((-1.5,1.5))

plt.legend()
plt.savefig('Upwind_burgers.png')
plt.clf()

for j in [0,0.1,0.25,0.5]:
	LW2(128,j)
	plt.title('Lax')
	plt.ylim((-1.5,1.5))

plt.legend()
plt.title('LaxWendroff_burgers')
plt.savefig('LaxWendroff_burgers.png')
plt.clf()

N=128
hx=1/N
ht=0.5*hx
x_arr = np.arange(0,1,hx)


for tstop in [0,0.1,0.25,0.5]:
	t_arr=np.arange(0,tstop,ht)
	uvec =np.array([uinit(x) for x in x_arr])
	for t in t_arr:
		uvec=lwvisc(uvec,128)
	plt.plot(x_arr,uvec,label='t='+str(tstop))
plt.legend()
plt.ylim((-1.5,1.5))
plt.title('Burgers, Lax-Wendroff with viscosity')
plt.savefig('burgers_LW_viscosity.png')