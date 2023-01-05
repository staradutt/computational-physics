import numpy as np

import matplotlib.pyplot as plt

def sqr(t):
	if -1<=t<0:
		return -1
	elif 0<=t<1:
		return 1
	else:
		print('invalid,outside domain')
def saw(t):
	return t
def mod_sin(t):
	return np.sin(np.pi*t)*np.sin(20*np.pi*t)
N=1000
x_arr=np.arange(-1,1,2/N)
x_arr1=np.arange(0,1,1/N)

k_arr=[i for i in range(len(x_arr))]
k_arr1=[i for i in range(len(x_arr1))]

kval=[abs(i) for i in np.fft.fft(np.vectorize(sqr)(x_arr))]
kval2=[abs(i) for i in np.fft.fft(np.vectorize(mod_sin)(x_arr1))]
kval3=[abs(i) for i in np.fft.fft(np.vectorize(saw)(x_arr))]


plt.plot(k_arr, kval)
plt.title('square_wave')
plt.savefig('square_wave.png')
plt.clf()
plt.plot(k_arr1, kval2)
plt.title('modulated sin')
plt.savefig('modulated_sin.png')
plt.clf()
plt.plot(k_arr, kval3)
plt.title('sawtooth')
plt.savefig('sawtooth.png')
plt.clf()



