import numpy as np 
import matplotlib.pyplot as plt 

pia=np.loadtxt('piano.txt')
tru=np.loadtxt('trumpet.txt')

c_pia=[abs(p) for p in np.fft.rfft(pia)]
c_tru=[abs(t) for t in np.fft.rfft(tru)]

k1=[i*44100/len(pia) for i in range(10000)]
k2=[i*44100/len(tru) for i in range(10000)]

plt.plot(k1[:10000],c_pia[:10000])
plt.xlabel('Freq.(Hz)')
plt.ylabel('coef.')
plt.title('piano')
plt.savefig('piano.png')
plt.clf()

plt.plot(k2[:10000],c_tru[:10000])
plt.xlabel('Freq. (Hz)')
plt.ylabel('coef.')
plt.title('trumpet')
plt.savefig('trumpet.png')
plt.clf()