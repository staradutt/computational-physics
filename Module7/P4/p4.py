import numpy as numpy
from math import sin 
import random

def func(x):
	return sin(1/(x*(2-x)))**2

A=2
N=10000
a,b=0,2
cnt_mc=0
funcsum=0
func2sum=0
for i in range(N):
	c1,c2=random.random()*2,random.random()
	y=func(c1)
	funcsum+=y
	func2sum+=y**2
	if c2<y:
		cnt_mc+=1


i1=cnt_mc*A/N
error1=(i1*(A-i1)/N)**0.5


i2=funcsum*(b-a)/N
var=(func2sum/N)-(funcsum/N)**2
error2=(b-a)*(var/N)**0.5



print('Hit and Miss method\n.............................')
print('value of integral = ',i1)
print('error = ',error1)
print('\n\nMean value method\n.............................')
print('value of integral = ',i2)
print('error = ',error2)