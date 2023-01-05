import numpy as np 
from matplotlib import pyplot as plt 
import math



def MB1(c,N):
	z=0+0j
	for i in range(N+1):
		if abs(z)>2:
			return 0
		z=(z**2)+c 
	return 1

def MB2(c,N):
	z=0+0j
	for i in range(N+1):
		if abs(z)>2:
			return i
		z=(z**2)+c 
	return N

def MB3(c,N):
	z=0+0j
	for i in range(N+1):
		if abs(z)>2:
			return math.log(i)
		z=(z**2)+c 
	return math.log(N)

x_arr=np.linspace(-2,-1.5,1001)
y_arr=np.linspace(-0.1,0.1,1001)

'''grid=[[MB1(x+y*1j,100) for x in x_arr] for y in y_arr]
plt.imshow(grid,cmap='hot',extent=(-500,500,-500,500))
plt.savefig('MBBinary')
plt.clf()

grid=[[MB2(x+y*1j,100) for x in x_arr] for y in y_arr]
plt.imshow(grid,cmap='hot',extent=(-500,500,-500,500))
plt.savefig('MB')
plt.clf()'''

grid=[[MB3(x+y*1j,100) for x in x_arr] for y in y_arr]
plt.imshow(grid,cmap='hot',extent=(-500,500,-500,500))
plt.savefig('MBLog(iter)')
plt.clf()