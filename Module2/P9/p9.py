import numpy as np 
from math import pi,sqrt,sin,cos
from matplotlib import pyplot as plt 
from gaussxw import gaussxwab
e0=8.85418782e-12
h=1e-7 #step size for calculating partial derivative
L=100e-2
q0=100
def potential(x,y):
	q1,q2=1,-1
	l1,l2=[5e-2,0],[-5e-2,0]
	r1,r2=sqrt(((l1[0]-x)**2)+((l1[1]-y)**2)),sqrt(((l2[0]-x)**2)+((l2[1]-y)**2))
	v1,v2=q1/(4*pi*e0*r1),q2/(4*pi*e0*r2)
	return v1+v2




x_arr1=np.linspace(-0.5,0.5,100)
y_arr1=np.linspace(-0.5,0.5,100)

grid1=[[potential(i,j) for i in x_arr1] for j in y_arr1 ]

plt.imshow(grid1)
plt.savefig('density_plot_dipole1.png')
plt.clf()
plt.contour(x_arr1,y_arr1,grid1,levels=1000)
plt.savefig('density_plot_dipole2.png')
plt.clf()

def partialx(func,x,y):
	return ( (func(x+h,y)-func(x,y))/h )
def partialy(func,x,y):
	return ( (func(x,y+h)-func(x,y))/h )
def Efield(func,x,y):
	return -partialx(func,x,y),-partialy(func,x,y) 
U=[]
V=[]
for m in y_arr1:
	urow=[]
	vrow=[]
	for n in x_arr1:
		vector=Efield(potential,n,m)
		urow.append(vector[0])
		vrow.append(vector[1])
	U.append(urow)
	V.append(vrow)
plt.streamplot(x_arr1,y_arr1,np.array(U),np.array(V),density=2,color='b')
plt.savefig('dipole_field.png')
plt.clf()

def sigma(x,y):
	return q0*sin(2*pi*x/L)*sin(2*pi*y/L)

def potential2(x1,y1):
	def funceval(x,y):
		return sigma(x,y)/4*pi*e0*sqrt((x-x1)**2+(y-y1)**2)
	val,wts=gaussxwab(20,-L/2,L/2)
	integral=0
	for i in range(len(val)):
		for j in range(len(val)):
			integral=integral+funceval(val[i],val[j])*wts[i]*wts[j]
	return integral
print('starting to compute electric field grid for square plate...')
print('please wait')
U2=[]
V2=[]
i=0
for m in y_arr1:
	urow=[]
	vrow=[]

	for n in x_arr1:
		vector=Efield(potential2,n,m)
		urow.append(vector[0])
		vrow.append(vector[1])
	U2.append(urow)
	V2.append(vrow)
	i+=1
	if i%10==0:
		print(i,'%  of field grid computed')
print('electric field grid computation completed')
plt.streamplot(x_arr1,y_arr1,np.array(U2),np.array(V2),density=2,color='b')
plt.savefig('field_sqr_plt.png')
plt.clf()







