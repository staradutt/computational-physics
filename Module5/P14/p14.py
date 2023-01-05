import numpy as np
import matplotlib.pyplot as plt
from math import e

u_0 = 1.0
v_0 = 0.0
start = 0
stop = 2.0

def f(r):
    u, v = r
    udot = 998*u + 1998*v
    vdot = -999*u - 1999*v
    return np.array([udot, vdot])



# forward euler
def forward(h):
    r = np.array([u_0, v_0])
    tpoints=[]
    u=[]
    v=[]
    t=start
    while t<stop:
        tpoints.append(t)
        u.append(r[0])
        v.append(r[1])
        r += h*f(r)
        t+=h

    plt.plot(tpoints, u, 'lightcoral', label='u (forward euler)')
    plt.plot(tpoints, v, 'lightgrey', label='v (forawrd euler)')
    plt.xlabel('t')
    plt.legend()
    plt.title('forward_h = '+str(h))
    plt.savefig('forward_ h ='+str(h)+'.png')
 

    plt.clf()


def backward(h):
    r = np.array([u_0, v_0])
    tpoints=[]
    u=[]
    v=[]
    t=start
    while t<stop:
        tpoints.append(t)
        u.append(r[0])
        v.append(r[1])
        r += h*f(r+h)
        t+=h

    plt.plot(tpoints, u, 'r', label='u (backward euler)')
    plt.plot(tpoints, v, 'lightskyblue', label='v (backward euler)')
    plt.xlabel('t')
    plt.legend()
    plt.title('backward_h = '+str(h))
    plt.savefig('backward_ h ='+str(h)+'.png')
    plt.clf()


forward(0.0001)
forward(0.002)
backward(0.0001)
backward(0.002)


x_arr=np.linspace(0,2,100)
u_arr=[2*e**(-x)-e**(-1000*x) for x in x_arr]
v_arr=[-(e**(-x))+e**(-1000*x) for x in x_arr]
plt.plot(x_arr,u_arr,label='u ')
plt.plot(x_arr,v_arr,label='v ')
plt.legend()
plt.title('analytical solution')
plt.savefig('analytic.png')

