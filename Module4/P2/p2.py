import numpy as np 
import matplotlib.pyplot as plt 
data=np.loadtxt('sunspots.txt')
t_arr=[]
n_arr=[]
for i in range(len(data)):
	t_arr.append(data[i][0])
	n_arr.append(data[i][1])
plt.plot(t_arr,n_arr)

plt.xlabel('month')
plt.ylabel('sunspot number')
plt.savefig('sunspot.png')
plt.clf()

c_arr=[abs(c)**2 for c in np.fft.rfft(n_arr)]
k_arr=[i for i in range(len(c_arr))]
plt.plot(k_arr,c_arr)

plt.xlabel('k')
plt.ylabel('coef. sqr.')
plt.savefig('power_spectrum.png')
plt.clf()