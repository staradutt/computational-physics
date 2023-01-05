# Problem - 11

import numpy as np
from matplotlib import pyplot as plt

el=1.60217662e-19
V0=50*el
a=1e-11
m=9.10938356e-31
hbar=6.62607004e-34 / (2 * np.pi)


def f1(v, x, E):
    y=v[0]
    y1=v[1]
    V=V0*(x**2/a**2)
    return np.array([y1, (2*m/hbar**2)*(V-E)*y])

def rk4(func, start, e_guess, x1, x2, h):
    y_arr = []
    x_arr = []
    x = x1
    y = start[0]
    y1 = start[1]
    E = e_guess
    v = np.array([y, y1])
    while x < x2:
        x_arr.append(x)
        y_arr.append(v[0])
        k1 = h * func(v, x, E)
        k2 = h * func(v + k1 / 2, x + h / 2, E)
        k3 = h * func(v + k2 / 2, x + h / 2, E)
        k4 = h * func(v + k3, x + h, E)
        v = v + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h
    return x_arr, y_arr

def shoot(e_range, func, step):
    le = e_range[0]
    ri = e_range[1]
    out1 = rk4(func, (0, 1), le, -10 * a, 10 * a, step * a)
    out2 = rk4(func, (0, 1), ri, -10 * a, 10 * a, step * a)
    if out1[1][-1] == 0:
        return out1, le
    elif out2[1][-1] == 0:
        return out2, ri
    mid = (le + ri) / 2
    out_mid = rk4(func, (0, 1), mid, -10 * a, 10 * a, step * a)
    while abs(out_mid[1][-1]) > 1e-10:
        if out_mid[1][-1] * out1[1][-1] > 0:
            le = mid
            out1 = rk4(func, (0, 1), le, -10 * a, 10 * a, step * a)
        elif out_mid[1][-1] * out2[1][-1] > 0:
            ri = mid
            out2 = rk4(func, (0, 1), ri, -10 * a, 10 * a, step * a)
        mid = (le + ri) / 2
        out_mid = rk4(func, (0, 1), mid, -10 * a, 10 * a, step * a)
    return out_mid, mid

def shoot2(e_range, func, step):
    le = e_range[0]
    ri = e_range[1]
    out1 = rk4(func, (0, 1), le, -5 * a, 5 * a, step * a)
    out2 = rk4(func, (0, 1), ri, -5 * a, 5 * a, step * a)
    

    if out1[1][-1] == 0:
        return out1, le
    

    elif out2[1][-1] == 0:
        return out2, ri
    mid = (le + ri) / 2
    out_mid = rk4(func, (0, 1), mid, -5 * a, 5 * a, step * a)
    


    while abs(out_mid[1][-1]) > 1e-10:
        if out_mid[1][-1] * out1[1][-1] > 0:
            le = mid
            out1 = rk4(func, (0, 1), le, -5 * a, 5 * a, step * a)
        

        elif out_mid[1][-1] * out2[1][-1] > 0:
            ri = mid
            out2 = rk4(func, (0, 1), ri, -5 * a, 5 * a, step * a)
        mid = (le + ri) / 2
        out_mid = rk4(func, (0, 1), mid, -5 * a, 5 * a, step * a)
    return out_mid, mid

def trapint(y_arr, x_arr):
    intg = 0
    N = len(x_arr)
    

    for i in range(1, N):
        intg += (y_arr[i - 1] ** 2 + y_arr[i] ** 2) * (x_arr[i] - x_arr[i - 1]) * 0.5
    

    return intg

def f2(v, x, E):
    y = v[0]
    y1 = v[1]
    V = V0 * (x ** 4 / a ** 4)
    return np.array([y1, (2 * m / hbar ** 2) * (V - E) * y])

out, E = shoot([100 * el, 200 * el], f1, 0.1)

plt.plot(out[0], out[1],'lightcoral')
plt.title("Energy = " + str(round(E / el,3)) + " eV")
plt.savefig("ground_state.png")
plt.clf()

out1, E = shoot([400 * el, 500 * el], f1, 0.1)
plt.plot(out1[0], out1[1],'lightcoral')
plt.title("Energy = " + str(round(E / el,3)) + " eV")
plt.savefig("1st_excited_state.png")
plt.clf()

out2, E = shoot([600 * el, 700 * el], f1, 0.1)
plt.plot(out2[0], out2[1],'lightcoral')
plt.title("Energy = " + str(round(E / el,3)) + " eV")
plt.savefig("2nd_excited_state.png")
plt.clf()

out3, E = shoot2([200 * el, 300 * el], f2, 0.1)
plt.plot(out3[0], out3[1],'lightcoral')
plt.title("Energy = " + str(round(E / el,3)) + " eV")
plt.savefig("ground_state(anh).png")
plt.clf()

out4, E = shoot2([700 * el, 800 * el], f2, 0.1)
plt.plot(out4[0], out4[1],'lightcoral')
plt.title("Energy = " + str(round(E / el,3)) + " eV")
plt.savefig("1st_excited_state_(anh).png")
plt.clf()

out5, E = shoot2([1400 * el, 1500 * el], f2, 0.1)

plt.plot(out5[0], out5[1],'lightcoral')
plt.title("Energy = " + str(round(E / el,3)) + " eV")
plt.savefig("2nd_excited_state_(anh).png")
plt.clf()


int3=trapint(out3[0], out3[1])
int4=trapint(out4[0], out4[1])
int5=trapint(out5[0], out5[1]) 
y1=out3[1]/int3
y2=out4[1]/int4
y3=out5[1]/int5



plt.plot(out3[0], y1,'lightcoral', label = "n = 0")
plt.title("Normalized WaveFn")
plt.savefig("Normalized_1.png")
plt.clf()
plt.plot(out4[0], y2,'lightcoral', label = "n = 1")
plt.title("Normalized WaveFn")
plt.savefig("Normalized_2.png")
plt.clf()
plt.plot(out5[0], y3,'lightcoral',label = "n = 2")
plt.title("Normalized WaveFn")
plt.savefig("Normalized_3.png")
plt.clf()


