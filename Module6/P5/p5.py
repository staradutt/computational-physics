import numpy as np
from matplotlib import pyplot as plt
from scipy.linalg import solve_banded

L=1e-8
m=9.109e-31
hbar=1.054e-34
x0=L/2
sigma=1e-10
k=5e10
def psi_arr_ini (x):
	return np.exp(-0.5*(x-x0)**2/sigma**2) * np.exp(1j*k*x)

xa=0.
xb=L
ta=0.
tb=1e-14
Nx=1000
ht=1e-18
hx=(xb-xa)/Nx

a1=1 + ht*1j*hbar/(2*m*hx**2)
a2=-ht*1j*hbar/(4*m*hx**2)
b1=1 - ht*1j*hbar/(2*m*hx**2)
b2=ht*1j*hbar/(4*m*hx**2)

x_arr=np.arange(xa,xb,hx)
t_arr=np.arange(ta,tb,ht)

n=np.size(x_arr)
A=np.zeros((n-2,n-2),dtype=complex)
psi_arr=psi_arr_ini(x_arr)

psi_arr[0]=0.
psi_arr[n-1]=0.

v=np.zeros(n,dtype=complex)

for i in range(n-2):
    

    if i==0:
        
        A[i,i]=a1
        A[i+1,i]=a2

    elif i==n-3:
        
        A[i,i]=a1
        A[i-1,i]=a2

    else:
        
        A[i,i]=a1
        A[i+1,i]=a2
        A[i-1,i]=a2





cnt=0
cnt2=0
for ti in range(len(t_arr)):
    for i in range(1,n-1):
        v[i]=b1*psi_arr[i]+b2*(psi_arr[i-1]+psi_arr[i+1])
        
    v1=v[1:n-1]
    u=1 
    AB=np.zeros((3,n-2),dtype=complex)
    for i in range (n-2):
        if i==0:
            
            AB[1,i]=A[i,i]
            AB[2,i]=A[i+1,i]
        
        elif i==n-3:
            
            AB[1,i]=A[i,i]
            AB[0,i]=A[i-1,i]
        
        else:
            
            AB[0,i]=A[i-1,i]
            AB[1,i]=A[i,i]
            AB[2,i]=A[i+1,i]
            
    psi_arr1 = solve_banded((1, 1), AB, v1)
    
    psi_arr[1:n-1] = psi_arr1
    
    if cnt%400==0:
        plt.figure(figsize=(8,8))
        plt.plot(x_arr,np.real(psi_arr))
        

        plt.ylabel(r'Re($\psi$)')
        plt.xlabel(r'x (m)')
        plt.title('t = '+str('%.2e'%t_arr[ti])+' sec')
        

        plt.ylim(-1.0,1.0)
        plt.savefig('wav'+str(cnt2)+'.png')
        plt.clf()
        plt.close()
        cnt2+=1
    
    cnt+=1