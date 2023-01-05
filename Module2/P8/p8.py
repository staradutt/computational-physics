# Problem - 16

from math import pi, e, sin, log, sqrt
import numpy as np 
from matplotlib import pyplot as plt 

d = 20e-6
W = 10 * d
lambd = 500e-9
L = 10e-2
f = 1

def q1(u):

    alpha = pi / d
    return (sin(alpha * u)) ** 2

def integrand(x, u, q):
 
    return (q(u) ** 0.5) * e ** ((2 * pi * x * u *1j) / (lambd * f))

def simp_int(func, N, begin, end):

    x = begin
    integral_val = func(begin) + func(end)
    interval = abs(end - begin) / N
    for i in range(1, N):
        x += interval
        if (i % 2):
            integral_val += 4 * func(x)
        else: 
            integral_val += 2 * func(x)
    integral_val = integral_val * (interval / 3)
    return integral_val
                                 
def Intensity(x, q, w):
    def f(t):
        return integrand(x, t, q)
    return abs(simp_int(f, 2000, -w / 2, w / 2)) ** 2




x_grid = np.linspace(-L / 2, L / 2, 1000)




#square root of intensity is plotted as it shows better contrast

int1grid = [(Intensity(x, q1, W))**0.5  for x in x_grid]
density_plot1 = [int1grid,] * 100
plt.imshow(density_plot1, cmap = "gray")
plt.title("Plot1")
plt.axis("off")
plt.savefig("plot1.png")

plt.clf()




def q2(u):

    alpha = pi / d
    beta = alpha / 2
    return (sin(alpha * u) * sin(beta * u)) ** 2

int2grid = [(Intensity(x, q2, W))**0.5  for x in x_grid]
density_plot2 = [int2grid,] * 100
plt.imshow(density_plot2, cmap = "gray")
plt.title("Plot2")
plt.axis("off")
plt.savefig("plot2.png")
plt.clf()


W1 = (10 + 20 + 60)*1e-6

def q3(u):

    if (-W1 / 2 <= u <= -W1 / 2 + 10e-6) or (-W1 / 2 + 70e-6 <= u <= -W1 / 2 + 90e-6):
        return 1
    else:
        return 0

int3grid = [(Intensity(x, q3, W1))**0.5  for x in x_grid]
density_plot3 = [int3grid,] * 100
plt.imshow(density_plot3, cmap = "gray")
plt.title("Plot3")
plt.axis("off")
plt.savefig("plot3.png")


