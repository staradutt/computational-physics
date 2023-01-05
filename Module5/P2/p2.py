import numpy as np 
from matplotlib import pyplot as plt 
al=1
be=0.5
ga=0.5
de=2

xi=2
yi=2

def f(x):
	return np.asarray([al*x[0]-be*x[0]*x[1],ga*x[0]*x[1]-de*x[1]])

a=0
b=50
N=1000
h=(b-a)/N
t_arr=np.arange(a,b,h)

x=[2.0,2.0]
x_arr=[]
y_arr=[]

for t in t_arr:
	x_arr.append(x[0])
	y_arr.append(x[1])
	
	k1=f(x)*h
	k2=h*f(x+0.5*k1)
	k3=h*f(x+0.5*k2)
	k4=h*f(x+k3)
	x+=(k1+2*k2+2*k3+k4)/6

plt.plot(t_arr,x_arr,'darkgrey',label='rabbits')
plt.plot(t_arr,y_arr,'lightcoral',label='foxes')
plt.legend()
plt.savefig('Lottka.png')






