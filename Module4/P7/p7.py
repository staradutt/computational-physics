import numpy as np 
from numpy import pi,sin
import matplotlib.pyplot as plt 

w=200e-6
W=10*w
D=10e-2
lambd=500e-9
f=1

N1=round(D/(lambd*f/w))
N2=round(D/(lambd*f/W))

def q(u):
	return sin((pi/20e-6)*u)**2

y_arr=[q(t*w/N1-w/2) for t in range(N1)]

for i in range(N2-N1):
	y_arr.append(0)

c_arr=np.fft.fft(y_arr)

i_arr=[((W**2/N2**2)*(abs(c_arr[int((t+N2/2)%N2)])**2))**0.5 for t in range(N2)]

img = np.tile(i_arr,(40,1))
plt.imshow(img,cmap='gray')
plt.savefig('diff_pattern.png')