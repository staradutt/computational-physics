from gaussxw import gaussxwab
from numpy import linspace
from matplotlib import pyplot as plt 
from math import pi


L=10
M=10e3
sigma=M/(L ** 2)
G=6.67408e-11

def function(x, y, z):
    
    return 1 / (x ** 2 + y ** 2 + z ** 2) ** 1.5

def forceval(z):

	values, weights = gaussxwab(100, 0, L / 2)
	I = 0
	for x in range(len(values)):
		for y in range(len(values)):
			I += function(values[x], values[y], z) * weights[x] * weights[y]
	return 4*G*sigma*z*I

z_arr = list(linspace(0, 10, 100))
z_arr.remove(0)
f_arr = [forceval(z) for z in z_arr]


plt.plot(z_arr, f_arr)
plt.xlabel('z')
plt.ylabel('force(in N)')
plt.savefig("force")
 

