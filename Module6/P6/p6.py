import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation as anim
import dcst

L=1e-8
m=9.109e-31
hbar=1.054e-34
x0=L/2
sigma=1e-10
k=5e10

def psi_ini (x):
    return np.exp(-0.5*(x-x0)**2/sigma**2)*np.exp(1j*k*x)

xa=0.
xb=L
ta=0.
tb=1e-14
Nx=1000

ht=1e-18
hx=(xb-xa)/Nx

x_arr=np.arange(xa,xb,hx)
t_arr=np.arange(ta,tb,ht)


psi_ini_arr=psi_ini(x_arr)
psi_ini_arr[0]=0.
psi_ini_arr[len(x_arr)-1]=0.



psi_real=np.real(psi_ini_arr)


psi_imag=np.imag(psi_ini_arr)

alpha_arr=dcst.dst(psi_real)


eta_arr=dcst.dst(psi_imag)

def psifunc (t):
    n_coeff=np.size(alpha_arr)
    coeff=np.zeros(n_coeff,dtype=float)    
    
    

    for k in range(n_coeff):
        
        th=np.pi**2*hbar*k**2*t/(2*m*L**2)
        
        coeff[k]=alpha_arr[k]*np.cos(th)-eta_arr[k]*np.sin(th)
    
    psi=dcst.idst(coeff)
    
    return psi
cnt=0


cnt2=0

for ti in range(np.size(t_arr)):    
    if ti==100:
        psi=psifunc(t_arr[ti])
        
        plt.figure(figsize=(8,8))
        plt.plot(x_arr,np.real(psi))
        plt.xlabel(r'x (m)')
        plt.ylabel(r'Re($\psi$)')
        
        plt.title('t = '+str('%.2e'%t_arr[ti])+' sec')
        plt.ylim(-1.0,1.0)
        plt.savefig('t_1e-16.png')
        
        plt.close()
    
    elif cnt%500==0:
        psi=psifunc(t_arr[ti])
        
        plt.figure(figsize=(8,8))
        plt.plot(x_arr,np.real(psi))
        plt.xlabel('x (m)')
        plt.ylabel(r'Re($\psi$)')
        
        plt.title('t = '+str('%.2e'%t_arr[ti])+' sec')
        plt.ylim(-1.0,1.0)
        plt.savefig('wav'+str(cnt2)+'.png')
        
        plt.close()
        
        cnt2+=1
    
    cnt+=1