from matplotlib import pyplot as plt
import numpy as np 

import time
t1=time.time()

N=100

maxiter=100000
#v initial
v=np.zeros(N**2)
for i in range(20*N,N**2-20*N):
	if i%N==20:
		v[i]=-1
	
	if i%N==79:
		v[i]=1
error=10
itr=0
while error>1e-6 and itr<maxiter :
	vprev=np.copy(v)
	for i in range(N,N**2-N):
		if (i>=20*N and i<N**2-20*N):  
			if i%N!=0 and i%N!=99 and i%N!=79 and i%N!=20:
				v[i]=0.25*(v[i-1]+v[i+1]+v[i+N]+v[i-N])
		else:
			v[i]=0.25*(v[i-1]+v[i+1]+v[i+N]+v[i-N])
	error=np.max(abs(v-vprev))
	itr +=1


print('time taken = ',time.time()-t1)
print('iterations = ',itr)
print('max error final = ',error)


grid=np.reshape(np.flip(v),(100,100))
plt.imshow(grid)
plt.colorbar()


plt.savefig('capacitor.png')
plt.savefig('capacitor.eps')





