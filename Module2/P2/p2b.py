import numpy as np 
from function import J
from math import sqrt,pi
from matplotlib import pyplot as plt 
lambd=0.5
k=(2*pi)/lambd
x_arr=np.linspace(-1,1,200)
y_arr=np.linspace(-1,1,200)
def intensity(x,y):
	kr=k*sqrt((x**2)+(y**2))
	I=(J(1,kr)/kr)**2
	return I

grid=[[intensity(x,y) for x in x_arr] for y in y_arr]
plt.imshow(grid,vmax=0.01,cmap='hot',extent=(-1,1,-1,1))
plt.xlabel('x in um')
plt.ylabel('y in um')
plt.savefig('diffraction pattern.png')
plt.clf()
