import numpy as np
from math import pi,sqrt,tan
from matplotlib import pyplot as plt
hcross=6.626e-34/(2*pi)
eV=1.60218e-19
V=20
m=9.1094e-31
w=1e-9


def evenE(E):  # Equation for even eigenstates
    return sqrt(E)*tan((sqrt(2*m*E*eV)*w)/(2*hcross))-sqrt(V-E)

def oddE(E):  # Equation for odd eigenstates
    return sqrt(E)/tan((sqrt(2*m*E*eV)*w)/(2*hcross))+sqrt(V-E)

def fp(f,a,b): # False position method 
    
    if f(a)*f(b)>0:
        return None
    else:
        i=0
        while(abs(b-a)>1e-4 and i<1000):
            c=(a*f(b)-b*f(a))/(f(b)-f(a))
            if f(a)*f(c)<0:
                b=c
            else:
                a=c
            i=i+1
        return c
    
E0=fp(evenE,0.25,0.35)
E1=fp(oddE,1.1,1.5)
E2=fp(evenE,2.4,3.3)
E3=fp(oddE,4,5.7)
E4=fp(evenE,6.9,8.2)
E5=fp(oddE,10.9,12.8)

#print(E0,E1,E2,E3,E4,E5)

f=open('out.txt', 'w')
f.write('Energy levels (in eV):\n')
f.write('\nE0 = '+str(E0))
f.write('\nE1 = '+str(E1))
f.write('\nE2 = '+str(E2))
f.write('\nE3 = '+str(E3))
f.write('\nE4 = '+str(E4))
f.write('\nE5 = '+str(E5))
f.close()
