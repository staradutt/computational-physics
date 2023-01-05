import matplotlib.pyplot as plt 
import numpy as np 

def func(x):
	return 924*x**6-2772*x**5+3150*x**4-1680*x**3+420*x**2-42*x+1
def derivf(x):
	return 5544*x**5-13860*x**4+12600*x**3-5040*x**2+840*x-42

x_arr=np.linspace(0,1,100)
y_arr=[func(x) for x in x_arr]
y2_arr=np.zeros(len(x_arr))
plt.plot(x_arr,y_arr)
plt.plot(x_arr,y2_arr)
plt.savefig('function.png')

tol=1e-14
maxiter=1000
def solve(func,guess):
	x=guess
	iter=0
	while abs(func(x)-x)>0 and iter<maxiter:
		x=x-func(x)/derivf(x)
		iter+=1
	return x
guess=[0.0,0.2,0.4,0.6,0.8,1.1]
sol=[solve(func,g) for g in guess]
f=open('out.txt','w')
for i in range(len(guess)):
	f.write('\n The '+str(i+1)+'th root is '+str(sol[i]))
f.close()


