import numpy as np 
from matplotlib import pyplot as plt 
import joblib 
from math import log

def bestfitslope(x,y):
	sigxy=[ x[i]*y[i] for i in range(len(x))]
	sigx2=[ x[i]**2 for i in range(len(x))]
	xym=np.mean(sigxy)
	xm=np.mean(x)
	ym=np.mean(y)
	x2m=np.mean(sigx2)
	
	m=(xym-xm*ym)/(x2m-xm**2)

	b=np.mean(y)-m*np.mean(x)
	return m,b

data=joblib.load('128.txt')
data1=joblib.load('256.txt')
data2=joblib.load('512.txt')
data3=joblib.load('1024.txt')
data4=joblib.load('0_025.txt')
data5=joblib.load('0.txt')



plt.plot(data5[0],data5[1],label='t = 0s')
plt.plot(data4[0],data4[1],label='t = 0.025s')
plt.legend()
plt.title('fx vs x at t = 0.025s, hx=1/256')
plt.savefig('fx_vs_x.png')
plt.clf()

#richardson 128
r128=0
for i in range(129):
	r128+=abs(data[1][i]-data1[1][2*i])
r128*=(1/(128+1))

r256=0
for i in range(257):
	r256+=abs(data1[1][i]-data2[1][2*i])
r256*=(1/(256+1))

r512=0
for i in range(513):
	r512+=abs(data2[1][i]-data3[1][2*i])
r512*=(1/(512+1))

logr_arr=[log(r128),log(r256),log(r512)]
loghx_arr=[log(x) for x in [data[2],data1[2],data2[2]]]

m,b =bestfitslope(loghx_arr,logr_arr)

x_arr=np.linspace(-6.5,-4.5)
y_arr=[m*x+b for x in x_arr]
plt.plot(x_arr,y_arr,'r',label='slope(bestfit) = '+str(round(m,4)))
label=['1/128','1/256','1/512']
for i in range(3):
	plt.scatter(loghx_arr[i],logr_arr[i],label='hx = '+str(label[i]))
plt.legend()
plt.xlabel('log \u0394x')
plt.ylabel('log (richardson L1)')
plt.savefig('logL1-log\u0394.png')
plt.clf()
