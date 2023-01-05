import numpy as np 
from math import e
from random import random as rnd 

def dist_func(x):
	return 1/(2*x**0.5)
def transform(z):
	return z**2
def func(x):
	return (x**(-0.5))/(e**x+1)

N=1000000
func_sum=0

for i in range(N):
	z=rnd()
	x=transform(z)
	func_sum+=func(x)/dist_func(x)
Intgl=func_sum/N

print('value of integral (by importance sampling, mean value method) = ',Intgl)