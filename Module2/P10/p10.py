

from math import factorial, pi, e

def cderiv(f, m, N):
    
    s = 0
    z = 1
    for k in range(N):
        h = e**((1j * 2 * pi * (k + 1)) / N) - e**((1j * pi * 2 * (k)) / N)
        s += f(z) * (e**((-1j * 2 * pi * k * m) / N))
        z += h
    deriv = (factorial(m) / N)*s
    return deriv

def function(var):
    return e**(2*var)

f = open("out.txt", 'w')
for i in range(1, 21):
    f.write("Derivative " + str(i) + "  =  " + str(cderiv(function, i, 10000)) + '\n')

f.write('\n\nThe accuracy for the derivatives are quite good.')
f.close()

