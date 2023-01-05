from math import exp,log,e
import numpy as np 
from matplotlib import pyplot as plt
from gaussxw import gaussxwab
def integrand(a,x):
	return x**(a-1)*exp(-x)
x_arr=np.linspace(0,5,100)
gamma2,gamma3,gamma4=[],[],[]

for i in range(len(x_arr)):
	gamma2.append(integrand(2,x_arr[i]))
	gamma3.append(integrand(3,x_arr[i]))
	gamma4.append(integrand(4,x_arr[i]))

plt.plot(x_arr,gamma2,label='gamma2')
plt.plot(x_arr,gamma3,label='gamma3')
plt.plot(x_arr,gamma4,label='gamma4')
plt.legend()
plt.savefig('plot')


def integrand2(a,z):
	c=a-1
	x=z*c/(1-z)
	return (c/((1-z)**2) )*e**(c*log(x)-x)

def ingl_quad(a):
	intgl=0
	val,wts=gaussxwab(1000,0,1)
	for i in range(len(val)):
		intgl+=integrand2(a,val[i])*wts[i]
	return intgl
f=open('out.txt','w')
f.write("Gamma function evaluations:\n.............................................")
f.write("\nGamma(3/2): " +str(round(ingl_quad(3/2),8)))
f.write("\nGamma(3): " +str(round(ingl_quad(3),8)))
f.write("\nGamma(6): " +str(round(ingl_quad(6),8)))
f.write("\nGamma(10): " +str(round(ingl_quad(10),8)))
f.close()
