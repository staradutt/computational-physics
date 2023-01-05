from matplotlib import pyplot as plt
import numpy as np

f=open('sunspots.txt')
raw=f.readlines()

x_arr=[]
y_arr=[]

for i in raw:
	x_arr.append(float(i.split()[0]))
	y_arr.append(float(i.split()[1]))
plt.plot(x_arr,y_arr)
plt.xlabel('month')
plt.ylabel('no of sunspots')
plt.savefig('part_a')
plt.xlim(right=1000,left=0)
plt.savefig('part_b')
r=5
xav=[]
yav=[]
for j in range(5,1001):
	y=0
	for i in range(-5,6):
		y=y+y_arr[j+i]
	y=y/(2*r)
	yav.append(y)
	xav.append(x_arr[j])
plt.plot(xav,yav,'r')
plt.xlim(left=5)
plt.savefig('part_c')
plt.clf()





