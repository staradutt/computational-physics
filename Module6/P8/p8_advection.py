import numpy as np 
from matplotlib import pyplot as plt 
from math import e,log
v=1
def sqr(x):
	if x>=0.6 and x<=0.8:
		return 1
	else:
		return 0
def inifunc(x):
	return e**( -200 * (x-0.3)**2 ) + sqr(x)

def Lax(N,tstop):
	hx=1/N
	x_arr=np.arange(0,1,hx)
	
	ht=0.5*hx/v
	f_arr=[inifunc(x) for x in x_arr]
	t=0
	
	while t<tstop:
		fcopy=np.copy(f_arr)
		
		for i in range(-1,N-1):
			
			f_arr[i]=0.5*(fcopy[i-1]+fcopy[i+1])-v*ht*(fcopy[i+1]-fcopy[i-1])/(2*hx)
		t+=ht
	
	return x_arr,f_arr,hx

def upwind(N,tstop):
	hx=1/N
	x_arr=np.arange(0,1,hx)
	
	ht=0.5*hx/v
	f_arr=[inifunc(x) for x in x_arr]
	t=0
	
	while t<tstop:
		fcopy=np.copy(f_arr)
		
		for i in range(-1,N):
			
			f_arr[i]=fcopy[i]-v*ht*(fcopy[i]-fcopy[i-1])/hx
				
		t+=ht
	return x_arr,f_arr,hx

def LW(N,tstop):
	hx=1/N
	x_arr=np.arange(0,1,hx)
	ht=0.5*hx/v
	f_arr=[inifunc(x) for x in x_arr]
	t=0
	while t<tstop:
		fcopy=np.copy(f_arr)
		for i in range(-1,N-1):
			m1=0.5*(fcopy[i]+fcopy[i-1])-0.5*v*ht*(fcopy[i]-fcopy[i-1])/hx
			m2=0.5*(fcopy[i+1]+fcopy[i])-0.5*v*ht*(fcopy[i+1]-fcopy[i])/hx
			f_arr[i]=fcopy[i]-v*ht*(m2-m1)/hx
		t+=ht
	return x_arr,f_arr,hx

def lwvisc_adv(u,n):
	v=1
	l = 0.923*hx
	ucopy = np.zeros(n,dtype=float)
	ucopy1 = np.zeros(n,dtype=float)


	udup1 = np.zeros(n,dtype=float)
	udup2 = np.zeros(n,dtype=float)
	
	for j in range(n):
		if u[j]<u[j-1]:
			ucopy[j] = (u[j]-u[j-1])/hx
		else:
			ucopy[j] = 0.
	temp = l**2 * ucopy**2 + v*u
	for j in range(-1,n-1):
		udup1[j] = 0.5*(u[j+1]+u[j]) - 0.5*ht*(temp[j+1]-temp[j])/hx
	for j in range(n):
		if udup1[j]<udup1[j-1]:
			ucopy1[j] = (udup1[j]-udup1[j-1])/hx
		else:
			ucopy1[j] = 0.
	temp2 = l**2 * ucopy1**2 + v*udup1
	for j in range(n):
		udup2[j] = u[j] - ht*(temp2[j]-temp2[j-1])/hx
	return udup2

def bestfitslope(x,y):
	sigxy=[ x[i]*y[i] for i in range(len(x))]
	sigx2=[ x[i]**2 for i in range(len(x))]
	xym=np.mean(sigxy)
	xm=np.mean(x)
	ym=np.mean(y)
	x2m=np.mean(sigx2)
	
	m=(xym-xm*ym)/(x2m-xm**2)

	
	return m


for i in [0,1,2,3]:
	x_arr,f_arr,hx=LW(128,i)
	plt.plot(x_arr,f_arr,label='lax-W')
	x_arr,f_arr,hx=Lax(128,i)
	plt.plot(x_arr,f_arr,label='lax')
	x_arr,f_arr,hx=upwind(128,i)
	plt.plot(x_arr,f_arr,label='upwind')
	plt.title('t = '+str(i))
	plt.legend()
	plt.savefig('Advection_t_'+str(i)+'.png')
	plt.clf()
	plt.close()



#richardson
grid_arr=[32,64,128,256,512,1024]
f_arrL=[]
f_arrLW=[]
f_arrU=[]
hxL=[]
hxLW=[]
hxU=[]


for i in grid_arr:
	data=Lax(i,1)
	f_arrL.append(data[1])
	hxL.append(data[2])

	data=LW(i,1)
	f_arrLW.append(data[1])
	hxLW.append(data[2])

	data=upwind(i,1)
	f_arrU.append(data[1])
	hxU.append(data[2])

#plot richardson upwind
richu=[]
richl=[]
richlw=[]
for i in range(5):
	richup=0
	richlax=0
	richlaxw=0
	for j in range(grid_arr[i]):
		richup+=abs(f_arrU[i][j]-f_arrU[i+1][2*j])
		richlax+=abs(f_arrL[i][j]-f_arrL[i+1][2*j])
		richlaxw+=abs(f_arrLW[i][j]-f_arrLW[i+1][2*j])
	richup*=(1/grid_arr[i])
	richlax*=(1/grid_arr[i])
	richlaxw*=(1/grid_arr[i])

	richu.append(log(richup))
	richl.append(log(richlax))
	richlw.append(log(richlaxw))
plt.plot([log(i) for i in hxU[:5]],richu,label='upwind',color='black')
plt.plot([log(i) for i in hxL[:5]],richl,label='Lax',color='lightskyblue')
plt.plot([log(i) for i in hxLW[:5]],richlw,label='Lax-W',color='red')
plt.xlabel('log(\u0394x)')
plt.ylabel('log(L1 error)')
plt.legend()

plt.title('log(L1 error) vs log(\u0394x) ')
plt.savefig('convergence.png')
plt.clf()
plt.close()

N=128
hx=1/N
ht=0.5*hx
x_arr = np.arange(0,1,hx)
t_arr=np.arange(0,1,ht)
uvec =np.array([inifunc(x) for x in x_arr])
plt.plot(x_arr,uvec,label='t = 0')
for i in range(3):
	
	
	for t in t_arr:
		uvec=lwvisc_adv(uvec,128)
	
	plt.plot(x_arr,uvec,label='t = '+str(i+1))
plt.legend()
plt.title('Advection,Lax-W with viscosity')
plt.savefig('Advection_with_viscosity.png')
plt.close()