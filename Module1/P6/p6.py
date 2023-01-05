from math import sqrt
import numpy as np

def Madelung(i,j,k):
	if i==0 and j==0 and k==0 :
		return 0
	return (((-1)**(i+j+k)) / sqrt(i**2 + j**2 + k**2))
L=100
M=0
for i in range(-L,L):
	for j in range(-L,L):
		for k in range(-L,L):
			M+=Madelung(i,j,k)
print('Madelung constant for NaCl = ',M,', for L = ',L)
print ()

f=open('output','w')
f.write('Madelung constant for NaCl = ' +str(M)+ ', for L = '+str(L))
f.close()