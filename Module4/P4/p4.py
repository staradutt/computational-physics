import numpy as np 
from math import floor
import matplotlib.pyplot as plt 

#part 1
dow1=np.loadtxt('dow.txt')

dowx=np.arange(len(dow1))
plt.plot(dowx,dow1)
plt.savefig('dow1.png')
plt.clf()

ffty=[c for c in np.fft.rfft(dow1)]

fft10=np.copy(ffty)
fft10[int(0.1*len(fft10)):]=0

fft2=np.copy(ffty)
fft2[int(0.02*len(fft2)):]=0

irfft10=[abs(c) for c in np.fft.irfft(fft10)]
irfft2=[abs(c) for c in np.fft.irfft(fft2)]




plt.plot(dowx,dow1,'lightskyblue',label='raw')
plt.plot(dowx,irfft10,'r',label='smoothed w 10%  Fourier terms')
plt.legend()
plt.savefig('10percent.png')
plt.clf()
plt.plot(dowx,dow1,'lightskyblue',label='raw')
plt.plot(dowx,irfft2,'r',label='smoothed w 2%  Fourier terms')
plt.legend()
plt.savefig('2percent.png')
plt.clf()

#part 2
sqr_x=np.arange(0,1,1/1000)
def sqr(t):
	if floor(2*t)%2==0:
		return 1
	else:
	 return -1
sqry=np.vectorize(sqr)(sqr_x)
fftsqr=np.fft.rfft(sqry)
fftsqr[10:]=0
irfftsqr=np.fft.irfft(fftsqr)
plt.plot(sqr_x,sqry)
plt.plot(sqr_x,irfftsqr)
plt.savefig('sqr_top10')
plt.clf()


