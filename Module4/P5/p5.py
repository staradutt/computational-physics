import dcst
import numpy as np 
import matplotlib.pyplot as plt 

dow1=np.loadtxt('dow2.txt')

dowx=np.arange(len(dow1))

ffty=np.fft.rfft(dow1)
csty=dcst.dct(dow1)

fft2=np.copy(ffty)
fft2[int(0.02*len(fft2)):]=0

cst2=np.copy(csty)
cst2[int(0.02*len(cst2)):]=0

irfft2=[abs(c) for c in np.fft.irfft(fft2)]
icst=dcst.idct(cst2)
plt.plot(dowx,dow1,'lightskyblue',label='Raw')
plt.plot(dowx,irfft2,'r',label='DFT smoothed')
plt.plot(dowx,icst,'black',label='DCT smoothed')
plt.legend()
plt.savefig('dow2.png')
plt.clf()