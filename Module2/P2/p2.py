from matplotlib import pyplot as plt 
from function import J
import numpy as np 

x_arr=np.linspace(0,20,100)
J0=[]
J1=[]
J2=[]
for i in range(len(x_arr)):
	J0.append(J(0,x_arr[i]))
	J1.append(J(1,x_arr[i]))
	J2.append(J(2,x_arr[i]))
plt.plot(x_arr,J0,label='J0')
plt.plot(x_arr,J1,label='J1')
plt.plot(x_arr,J2,label='J2')
plt.legend()
plt.savefig('plot1')
plt.clf()
m=[]
y=np.linspace(0.01,1)
for i in range(len(y)):
	m.append(J(1,y[i])/y[i])
plt.plot(y,m)
plt.show()
