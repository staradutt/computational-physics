
import numpy as np 
from matplotlib import pyplot as plt 
import time
import joblib
def tridi_sol(A,b):
	#array creation starts
	N=len(A)
	b_arr=np.copy(b)
	x_arr=np.zeros(N)
	f_arr=[]
	e_arr=[]
	g_arr=[]

	for i in range(N):
		f_arr.append(A[i][i])
		if i!=N-1:
			g_arr.append(A[i][i+1])
			e_arr.append(A[i+1][i])
	#array creation ends
	
	#step 1
	for i in range(1,N):
		temp=e_arr[i-1]/f_arr[i-1]
		f_arr[i]=f_arr[i]-temp*g_arr[i-1]
		b_arr[i]=b_arr[i]-temp*b_arr[i-1]
	#back substitution
	x_arr[N-1]=b_arr[N-1]/f_arr[N-1]
	for i in range(N-2,-1,-1):
		x_arr[i]=(b_arr[i]-g_arr[i]*x_arr[i+1])/f_arr[i]
	return x_arr

D=1
def fval(x):
	if x>0.4 and x<0.6:
		return 1
	else:
		return 0
def solver(N,tstop):
	x_arr=np.linspace(0,1,N)
	hx=x_arr[1]-x_arr[0]
	ht=(4*hx**2)/D
	
	#constructing the matrix A&uvt 
	diag=1+2*D*ht/hx**2
	off_diag=-D*ht/hx**2
	
	A=np.zeros((N,N))

	for i in range(N):
		A[i][i]=diag
		if i!=N-1:
			A[i+1][i]=off_diag
			A[i][i+1]=off_diag
	#creation of A
	A[0][0]=A[0][0]-off_diag
	A[N-1][N-1]=A[N-1][N-1]-off_diag

	#creation of u and v
	uvec=np.zeros(N)
	vvec=np.zeros(N)
	for i in [0,N-1]:
		uvec[i]=off_diag
		vvec[i]=1.

	#initial function value vector at t=0
	func_arr=[fval(x) for x in x_arr]
	t=0
	#count=0
	while t<tstop:
		
		y=tridi_sol(A,func_arr)
		q=tridi_sol(A,uvec)
		func_arr=y-q*(np.matmul(vvec,y)/(1+np.matmul(vvec,q)))
		t+=ht

		#count+=1
	return x_arr,func_arr,hx
t1=time.time()

x_arr2,func_arr2,hx2=solver(257,0)
print('calculation for initial, hx = 1/256 done')
print(time.time()-t1)
joblib.dump([x_arr2,func_arr2,hx2],'0.txt')


x_arr1,func_arr1,hx1=solver(129,1)
print('calculation for hx = 1/128 done')
print(time.time()-t1)
joblib.dump([x_arr1,func_arr1,hx1],'128.txt')


x_arr2,func_arr2,hx2=solver(257,1)
print('calculation for hx = 1/256 done')
print(time.time()-t1)
joblib.dump([x_arr2,func_arr2,hx2],'256.txt')


x_arr3,func_arr3,hx3=solver(513,1)
print('calculation for hx = 1/512 done')
print(time.time()-t1)
joblib.dump([x_arr3,func_arr3,hx3],'512.txt')


x_arr4,func_arr4,hx4=solver(1025,1)
print('calculation for hx = 1/1024 done')
print(time.time()-t1)
joblib.dump([x_arr4,func_arr4,hx4],'1024.txt')

t1=time.time()
x_arr1,func_arr1,hx1=solver(129,1)
print('calculation for t = 0.025 done')
print(time.time()-t1)
joblib.dump([x_arr1,func_arr1,hx1],'0_025.txt')

#plt.legend()
#plt.show()








