import numpy as np
from matplotlib import pyplot as plt

inc=0.01
r_arr=np.arange(1,4,inc)
x_arr=0.5*np.ones(len(r_arr))

for r in r_arr:
	x=0.5
	xtemp=[]
	for i in range(1000):
		x=x*r*(1-x)
		xtemp.append(x)
	plt.scatter(r*np.ones(len(xtemp)),xtemp,marker='.')
plt.xlabel('r')
plt.ylabel('x')
plt.title('FigenBaum1')
plt.grid(True)
plt.savefig('FigenBaum1')
plt.clf()

for i in range(1000):
	x_arr=r_arr*x_arr*(1-x_arr)
	plt.scatter(r_arr,x_arr,marker='.')
plt.xlabel('r')
plt.ylabel('x')
plt.title('FigenBaum2')
plt.grid(True)
plt.savefig('FigenBaum2(AltMethod)')

plt.clf()
f=open('output','w')
f.write('partA\n\n')
f.write('''A fixed point appears as an isolated point in the entire column of points for 
a given value of r. A limit cycle repeatedly cycles between limit values, so they appear 
as discrete points contained in a column of fixed height. Chaos is quite random and takes 
unique values in each iteration,so they are randomly scattered on the column with fixed r.''')
f.write('\n\npartB\n\n')
f.write('''The edge of chaos is around r = 3.5 as can be seen from gridlines of the plot. After that it becomes chaotic.''')
f.close()