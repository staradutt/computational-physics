import numpy as np
import math 

def f(x):
    return np.sin(np.sqrt(100 * x)) ** 2

def tzl(f, a, b, N):
    x = a
    I = f(a) + f(b)
    dx = abs(b-a)/N
    for i in range(1, N):
        x += I
        I += 2 * f(x)
    I *= dx / 2
    return I


def adaptive_trap(f, a, b, tol):
    mid = (b+a)/2

    I1 = tzl(f, a, mid, 1)
    I2 = tzl(f,mid, b, 1)
    I = tzl(f, a, b, 1)
    err = abs(I - (I1 + I2))
    arr = [a, mid, b]
    print("N \t Error \t\t I \n")
    print("%i \t %f \t %f \n" %(1, err, I))
    while err > tol:
        I = 0
        err = 0
        tol_i = 0
        l = np.size(arr)
        for i in range(l - 1):
            I_i =  tzl(f, arr[i], arr[i + 1], 1)
            
            tol_i = tol * ((arr[i + 1] - arr[i]) / (b-a))
            
            mid = (arr[i] + arr[i + 1]) / 2
            
            ileft = tzl(f, arr[i], mid, 1)
            iright = tzl(f, mid, arr[i + 1], 1)
            
            err_i = abs(I_i - ileft - iright)
            I += ileft + iright
            
            err += err_i
            if err_i > tol_i:
                arr.append(mid)
        print("%i \t %.7f \t%.7f\n" %(l - 1, err, I))
        arr.sort()
    return I

def romberg_trap(f, a, b, tol):
    I0 = tzl(f, a, b, 1)
    r_arr = [[I0]]
    i = 1
    while True:
        I = tzl(f, a, b, 2**i)
        r_arr.append([I])
        j = 0
        while len(r_arr[i]) <= len(r_arr[i - 1]):
            r_arr[i].append(((4**(j + 1)) * r_arr[i][j] - r_arr[i - 1][j]) / (4 ** (j + 1) - 1))
            j += 1
        err = abs(r_arr[i][j] - r_arr[i][j - 1])
        if err < tol:
            break
        i += 1
    return r_arr

def coef(n,N):
    if (n == 0 or n==N-1):
        return 1.0
    else:
        if (n%2 == 0):
            return 2.0
        else:
            return 4.0
def simpson_N (f,a,b,N):
    dx = (b-a)/N
    s = 0
    for i in range(N):
        x = a + i*dx
        s = s + coef(i,N)*f(x)
    
    return dx*s/3

def simpson (f,a,b):
    c = (b+a)/2
    dx = abs(b-a)/6
    I = f(a) + 4*f(c) + f(b)
    return dx*I

def adaptive_simpson(f, a, b, tol):
    mid = (b+a)/2

    I1 = simpson(f, a, mid)
    I2 = simpson(f, mid, b)
    I = simpson(f, a, b)
    err = abs(I - (I1 + I2))
    p = [a, mid, b]
    print("N \t Error \t\t I \n")
    print("%i \t %f \t %f \n" %(1, err, I))
    while err > tol:
        I = 0
        err = 0
        tol_i = 0
        l = np.size(p)
        for i in range(l - 1):
            I_i = simpson(f, p[i], p[i + 1])
            
            tol_i = tol * ((p[i + 1] - p[i]) / (b-a))
            
            mid = (p[i+1] + p[i])/2
            
            il = simpson(f, p[i], mid)
            ir = simpson(f, mid, p[i+1])
            
            err_i = abs(I_i - il -ir)
            I += il + ir
            
            err += err_i
            if err_i > tol_i:
                p.append(mid)
        print("%i \t %.7f \t%.7f\n" %(l - 1, err, I))
        p.sort()
    return I,p

def romberg_simpson(f, a, b, tol):
    I0 = simpson(f, a, b)
    r_arr = [[I0]]
    i = 1
    while True:
        I = simpson_N(f, a, b, 2**i)
        r_arr.append([I])
        j = 0
        while len(r_arr[i]) <= len(r_arr[i - 1]):
            r_arr[i].append(((4**(j + 1)) * r_arr[i][j] - r_arr[i - 1][j]) / (4 ** (j + 1) - 1))
            j += 1
        err = abs(r_arr[i][j] - r_arr[i][j - 1])
        if err < tol:
            break
        i += 1
    return r_arr

print("\nAdaptive trapezoidal Integration \n....................................................\n")
I_trap= adaptive_trap(f, 0, 1, 1e-6)


print("\n\nRomberg Integration for trapezoidal method \n....................................................\n")
r_trap = romberg_trap(f, 0, 1, 1e-6)

for k in range(len(r_trap)):
        print(str(2 ** k),end='\t')
        for l in range(len(r_trap[k])):
            print("%f" %(r_trap[k][l]),end='\t')
        print('\n')
        
print("Adaptive Simpson Integration \n....................................................\n")
I_simp, p_simp = adaptive_simpson(f, 0, 1, 1e-6)


print("\n\nRomberg Integration for Simpson method \n....................................................\n")
rsimp = romberg_simpson(f, 0, 1, 1e-6)
for k in range(len(rsimp)):
        print(str(2 ** k),end='\t')
        for l in range(len(rsimp[k])):
            print("%f" %(rsimp[k][l]),end='\t')
        print('\n')