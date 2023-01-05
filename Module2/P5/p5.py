from math import exp,pi,sqrt,tan,cos,sin,factorial
import numpy as np 
from matplotlib import pyplot as plt
from gaussxw import gaussxwab 
def H(n,x):
	if n==0:
		return 1
	if n==1:
		return 2*x
	if n<=0 or n%1!=0:
		return 0
	else:
		temp1=1
		temp2=2*x
		i=2
		while i<=n:
			temp1,temp2=temp2, 2*x*temp2 - 2*(i - 1)*temp1
			i+=1
	return temp2

def psi(n,x):
	return (H(n,x)*exp(-0.5*x**2))/sqrt( 2**n * factorial(n) * sqrt(pi)    )
x_arr=np.linspace(-4,4,1000)
x_arr1=np.linspace(-10,10,1000)
wf0=[]
wf1=[]
wf2=[]
wf3=[]
wf30=[]
for x in x_arr:
	wf0.append(psi(0,x))
	wf1.append(psi(1,x))
	wf2.append(psi(2,x))
	wf3.append(psi(3,x))
plt.plot(x_arr,wf0,label='wf0')
plt.plot(x_arr,wf1,label='wf1')
plt.plot(x_arr,wf2,label='wf2')
plt.plot(x_arr,wf3,label='wf3')
plt.legend()
plt.savefig('wave_fn_plots.png')
plt.clf()

for x in x_arr1:
	wf30.append(psi(30,x))
plt.plot(x_arr1,wf30)
plt.title('wf30')
plt.savefig('wf30.png')
plt.clf()

def rmspos(n):
	def integrand(n,phi):#variable change x=tan phi to cover -inf to +inf
		if abs(phi) == pi/2:
			return 0
		else:
			return (tan(phi) * psi(n, tan(phi)) * (1 / cos(phi))) ** 2
	val,wts=gaussxwab(100,-pi/2,pi/2)
	integral=0
	for i in range(len(val)):
		integral+=integrand(n,val[i])*wts[i]
	return (integral)**0.5

f=open('out.txt','w')
f.write('uncertainty in pos for n=5 is '+str(rmspos(5)))
f.close()







