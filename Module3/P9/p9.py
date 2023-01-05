#import matplotlib.pyplot as plt
G=6.674e-11
M=5.974e24
m=7.248e22
R=3.844e8
w=2.662e-6

def orbitFunc(r):#eqn of orbit at lagrange point
	return G*((M/(r**2))-(m/(R-r)**2))-(w**2)*r
# Plotting for a guess value
"""
N = 1000
a = 3e8
b = 3.5e8
x_arr = np.arange(a, b, (b - a) / N)
y_arr = [orbitFunc(x) for x in x_arr]

y1_arr = [0, ] * len(x_arr)

plt.plot(x_arr, y_arr)

plt.plot(x_arr, y1_arr)

plt.show()
"""
# Approximate value of r = 3.3e8
	
def solve(f, gs1, gs2, tol):
	x1 = gs1
	x2 = gs2
	while (abs(f(x2)) > tol):
		x1,x2 =x2,(x1*f(x2)-x2*f(x1))/(f(x2)-f(x1))
	return x2
f=open('out.txt','w')
f.write("Distance (r) of L1 point is: " + str(round(solve(orbitFunc, 3.2e8, 3.6e8, 1e-14) * 1e-8, 4)) + "e8 metres\n")
f.write("Ratio of distance of L1 point to R: " + str(solve(orbitFunc, 3.2e8, 3.6e8, 1e-14)/ R) + '\n')
f.close()