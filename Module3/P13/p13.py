#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 23:04:20 2020

@author: hitesh
"""

import numpy as np

A = np.array([[1,4,8,4],[4,2,3,7],[8,3,6,9],[4,7,9,2]])

N = np.shape(A)[0]

def QR (A):
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

def tol_arr(A):
    t_arr = A
    for i in range(N):
        t_arr[i,i] == 0
    return t_arr

Ak = np.copy(A)
Ak1 = np.copy(A)
tol = 1e-1
EV = np.identity(N)

for i in range(10000):
    Q, R = QR (Ak)
    Ak = np.matmul(R,Q)
    EV = np.matmul(EV,Q)

E_vec = EV

f=open('out.txt','w')
f.write('Calculated Eigenvalues:\n')
for i in range(N):
    f.write(str(Ak[i,i]))
    f.write('\n')
f.write("\nEigenvalues from numpy eig function:\n")
f.write(str(np.linalg.eig(A)[0]))

f.write("\nComputed eigenvectors:\n")
for i in range(N):
    f.write(str(E_vec[:,i]))
    f.write('\n')
f.write("\nEigenvectors from numpy eig function:\n")
for i in range(N):
    f.write(str(np.linalg.eig(A)[1][i]))
    f.write('\n')
f.write('\nValues computed by the program are comparable to numpy.linalg.eig function')
f.close()