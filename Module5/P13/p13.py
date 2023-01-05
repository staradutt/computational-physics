import numpy as np 
from matplotlib import pyplot as plt 
N=3
def f(x,t):
	# x=[m,theta]
	m=x[0]
	tht=x[1]
	return np.array([ t**2 * tht**N, -m/t**2 ])
tol=1e-3
def shoot(tht_guess,epsilon,stop,h):
	m_arr=[]
	tht_arr=[]
	t_arr=[]
	t=epsilon
	
	x=np.array([tht_guess**3*epsilon**3,tht_guess])

	while t<stop and abs(x[1]-0)>tol:
		m_arr.append(x[0])
		tht_arr.append(x[1])
		t_arr.append(t)
		k1=h*f(x,t)
		k2=h*f(x+0.5*k1,t+0.5*h)
		k3=h*f(x+0.5*k2,t+0.5*h)
		k4=h*f(x+k3,t+h)
		x+=(k1+2*k2+2*k3+k4)/6
		t+=h
	return m_arr,tht_arr,t_arr
	
for i in range(8):
	m_arr,tht_arr,t_arr=shoot(i,0.001,10,0.001)
	#plt.plot(t_arr,m_arr,label='m')
	plt.plot(t_arr,tht_arr,label='\u03B8 guess='+str(i))
	plt.legend()
plt.axvline(x=2)
plt.ylabel(u"\u03B8")
plt.xlabel(u"\u03BE")
plt.savefig('\u03B8 vs \u03BE.png')
plt.clf()


def shoot2(tht_guess):

	t=0.001
	h=0.001
	x=np.array([tht_guess**3*t**3,tht_guess])
	tol=1e-3
	while t<10 and abs(x[1]-0)>tol:

		k1=h*f(x,t)
		k2=h*f(x+0.5*k1,t+0.5*h)
		k3=h*f(x+0.5*k2,t+0.5*h)
		k4=h*f(x+k3,t+h)
		x+=(k1+2*k2+2*k3+k4)/6
		t+=h
	return t-2
def deriv(x):
	h=1e-2
	return (shoot2(x+h)-shoot2(x))/h	
def NR(tht_guess):
	tol=1e-6
	maxiter=100
	x=tht_guess
	i=0
	print('iteration','   value of \u03B8 initial')
	while abs(shoot2(x))>tol and i<maxiter:
		
		print(i,'         ',round(x,5))
		x=x-(shoot2(x)/deriv(x))
		i+=1
		
	return x

NR(1.5)

