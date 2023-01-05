import numpy as np 
from numpy import e 
import matplotlib.pyplot as plt 

raw=np.loadtxt('blur.txt')

plt.imshow(raw,cmap='gray')
plt.axis('off')
plt.savefig('raw.png')
plt.clf()

def gaus2D(x,y,z):
	return e**(-(x**2 + y**2) / 2*z**2)

a=1.705
pt_sprd=[[gaus2D(((i+512)%1024-512)*a/1024, ((j+512)%1024-512)*a/1024, 25) for i in range(1024)] for j in range(1024)]

plt.imshow(pt_sprd,cmap='gray')

bfft = np.fft.fft2(raw)
pfft = np.fft.fft2(pt_sprd)
a_2darr = []

for i in range(1024):
	row=[]
	for j in range(1024):
		if abs(pfft[i][j])>1e-3:
			row.append(bfft[i][j]/pfft[i][j])
		else:
			row.append(bfft[i][j])
	a_2darr.append(row)

im=[t.real for t in np.fft.ifft2(a_2darr)]
plt.imshow(im, cmap = 'gray')
plt.axis('off')
plt.savefig('after_processing.png')