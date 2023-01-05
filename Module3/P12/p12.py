#!/usr/bin/env python3
import numpy as np

N = 200

B = 2 * np.diag(np.full(N,1.0)) + np.random.rand(N, N)/((200) ** 0.5)

A = (B + np.transpose(B)) / 2
A_temp = (B + np.transpose(B)) / 2
A_temp2 = (B + np.transpose(B)) / 2

def lu_decomp (A): # LU Decomposition
    U = A    
    L = np.identity(N)
    m = N    
    for k in range(m):
        for j in range(k + 1, m):
            L[j,k] = U[j,k] / U[k,k]
            U[j,k:m] = U[j,k:m] - L[j][k] * U[k,k:m]
    return L, U

def qr_decomp (A):#qr factorisation
	v=np.zeros((N,N),dtype=float)
	q = np.copy(v)
	r = np.copy(v)
	for i in range(N):
		v[:,i] = A[:,i]
	for i in range(N):
		r[i,i] = np.sqrt(np.dot(v[:,i], v[:,i]))
		q[:,i] = v[:,i]/r[i,i]
		for j in range(i + 1, N):
			r[i,j] = np.dot(q[:,i], v[:,j])
			v[:,j] = v[:,j]-r[i,j]*q[:,i]
	return q,r

L, U = lu_decomp(A_temp)
Q, R = qr_decomp(A_temp2)


b = np.zeros(N,dtype=float) + 1.0
y = np.zeros(N,dtype=float)

for i in range(N):
    s = 0
    for j in range(i):
        s += L[i,j] * y[j]
    val = ((b[i] - s) / L[i,i])
    y[i] = val

x = np.zeros(N,dtype=float)

M = N - 1

for i in range(N):
    s = 0
    for j in range(i):
        s += U[M - i,M - j] * x[M - j]
    val = ((y[M - i] - s) / U[M - i,M - i])
    x[M - i] = val
f=open('out.txt','w')
f.write("LU Decomposition result:\n")
f.write("i \t   x\n")
for i in range (N):
    f.write(str(i)+' '+str(x[i])+'\n')
    
y_1 = np.dot(np.transpose(Q),b)
x_1 = np.zeros(N,dtype=float)

for i in range(N):
    s = 0
    for j in range(i):
        s += R[M - i,M - j] * x_1[M - j]
    val = ((y_1[M - i] - s) / R[M - i,M - i])
    x_1[M - i] = val

f.write('\n')
f.write("From QR Decomposition result:\n")
f.write("i \t   x\n")
for i in range (N):
    f.write(str(i)+' '+str(x_1[i])+'\n')
f.write('\nfrom both LU and QR we get similar results')
f.close()