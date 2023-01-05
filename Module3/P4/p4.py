import matplotlib.pyplot as plt 
import numpy as np 
from math import e 

f=open('out.txt','w')
def func(x,c):
	return 1-(e**(-c*x))

def solve(func,c,guess,tol,disp=False):
	x=guess
	i=0
	while abs(func(x,c)-x)>tol:
		if disp:
			f.write(str(i)+'    '+str(x)+'\n')
		x=func(x,c)
		i+=1

	return x
c_arr=np.arange(0,3.01,0.01)
x_arr=[]
for i in range(len(c_arr)):
	x_arr.append(solve(func,c_arr[i],1,1e-6))
plt.plot(c_arr,x_arr)
plt.xlabel('c')
plt.ylabel('x')
plt.title('c vs x')
plt.savefig('c-x_curve.png')

#accelerated fixed point iteration 
#g(x)=x-f(x)
def gderiv(x,c):
	return 1-c*e**(-c*x)
guess=1
def func2(x,c):
	return x+(-1/gderiv(guess,2))*(x-func(x,c))
f.write('\npart a\n\n')
f.write('iteration    x\n\n')
r1=solve(func,2,1,1e-6,True)
f.write('root is '+str(round(r1,6))+'calculated till 10^(-6) precision')
f.write('\n\npart c\n\n')
f.write('iteration    x\n\n')
r2=solve(func2,2,1,1e-6,True)
f.write('root is '+str(round(r2,6))+'calculated till 10^(-6) precision')
f.write('\n\nclearly less iterations in accelerated case.')
f.close()