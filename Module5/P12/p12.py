import numpy as np 
from matplotlib import pyplot as plt 

m1=150
m2=200
m3=250
G=1
delta=1e-5

def f(x):
	x1=x[0]
	y1=x[1]
	x1d=x[2]
	y1d=x[3]
	x2=x[4]
	y2=x[5]
	x2d=x[6]
	y2d=x[7]
	x3=x[8]
	y3=x[9]
	x3d=x[10]
	y3d=x[11]
	derv1=[x1d,y1d,G*m2*(x2-x1)/((x2-x1)**2+(y2-y1)**2)**1.5+G*m3*(x3-x1)/((x3-x1)**2+(y3-y1)**2)**1.5,G*m2*(y2-y1)/((x2-x1)**2+(y2-y1)**2)**1.5+G*m3*(y3-y1)/((x3-x1)**2+(y3-y1)**2)**1.5]
	derv2=[x2d,y2d,G*m3*(x3-x2)/((x3-x2)**2+(y3-y2)**2)**1.5+G*m1*(x1-x2)/((x1-x2)**2+(y1-y2)**2)**1.5,G*m3*(y3-y2)/((x3-x2)**2+(y3-y2)**2)**1.5+G*m1*(y1-y2)/((x1-x2)**2+(y1-y2)**2)**1.5]
	derv3=[x3d,y3d,G*m1*(x1-x3)/((x1-x3)**2+(y1-y3)**2)**1.5+G*m2*(x2-x3)/((x2-x3)**2+(y2-y3)**2)**1.5,G*m1*(y1-y3)/((x1-x3)**2+(y1-y3)**2)**1.5+G*m2*(y2-y3)/((x2-x3)**2+(y2-y3)**2)**1.5]
	return np.array(derv1+derv2+derv3)

def adptRK4(xinitial,start,stop,hin):
	x1_arr=[]
	y1_arr=[]
	x2_arr=[]
	y2_arr=[]
	x3_arr=[]
	y3_arr=[]
	h=hin
	maxh=5*h
	x=xinitial
	t=start
	while t<stop:
		x1_arr.append(x[0])
		y1_arr.append(x[1])
		x2_arr.append(x[4])
		y2_arr.append(x[5])
		x3_arr.append(x[8])
		y3_arr.append(x[9])
		#estimate by single step
		k1=2*h*f(x)
		k2=2*h*f(x+0.5*k1)
		k3=2*h*f(x+0.5*k2)
		k4=2*h*f(x+k3)
		xt2h_est2=x+(k1+2*k2+2*k3+k4)/6
		#estimate by double step
		for i in range(2):
			k1=h*f(x)
			k2=h*f(x+0.5*k1)
			k3=h*f(x+0.5*k2)
			k4=h*f(x+k3)
			x+=(k1+2*k2+2*k3+k4)/6
			t+=h
		xt2h_est1=x		
		
		diff=(np.sum(np.array([(xt2h_est1[i]-xt2h_est2[i])**2 for i in[0,1,4,5,8,9]])))**0.5
		
		h*=((30*h*delta)/(diff))**0.25
		if h>=maxh:
			h=maxh
	
	return x,np.array([x1_arr,y1_arr,x2_arr,y2_arr,x3_arr,y3_arr])

final,data=adptRK4([3,1,0,0,-1,-2,0,0,-1,1,0,0],0,2,0.01)
plt.scatter(data[0],data[1],marker='.',label='m1')
plt.scatter(data[2],data[3],marker='.',label='m2')
plt.scatter(data[4],data[5],marker='.',label='m3')
plt.scatter([3,-1,-1],[1,-2,1],color='r',marker='.',label='initial_pos')
plt.scatter([final[i] for i in [0,4,8]],[final[i] for i in [1,5,9]],color='black',marker='.',label='final_pos')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('3body_adaptiveRK4')
plt.savefig('3body_adaptiveRK4.png')
plt.clf()