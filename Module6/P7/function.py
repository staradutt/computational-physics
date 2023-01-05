import numpy as np 


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


