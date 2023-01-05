import numpy as np 
import matplotlib.pyplot as plt 
from numpy import pi,e

pitch=np.loadtxt('pitch.txt')

def fft(arr):
	

	N = len(arr)
	

	if N == 1:
		return arr
	

	c_arr = [0 for i in range(N)]
	

	ev_arr = []
	od_arr = []
	

	for i in range(N):
		

		if i%2==0:
			ev_arr.append(arr[i])
		elif i%2==1:
			od_arr.append(arr[i])
	
	c_even = fft(ev_arr)
	c_odd = fft(od_arr)

	for t in range(int(N/2)):
		c_arr[t]=c_even[t]+e**(-1j * 2*pi*t/N)*c_odd[t]
		c_arr[t+int(N/2)]=c_even[t]- e**(-1j*2*pi*t/N)*c_odd[t]
	return c_arr

fft_computed=[abs(c) for c in fft(pitch)]
fft_np=[abs(c) for c in np.fft.fft(pitch)]
k_arr=np.arange(len(fft_computed))

plt.plot(k_arr,fft_computed,'r')
plt.title('fft computed by user def function')
plt.savefig('fft_user.png')
plt.clf()

plt.plot(k_arr,fft_np,'black')
plt.title('fft computed by np.fft')
plt.savefig('fft_numpy.png')
plt.clf()