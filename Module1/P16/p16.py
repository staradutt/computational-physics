import numpy as np
from matplotlib import pyplot as plt

data=np.loadtxt('millikan.txt')

x_arr=[]
y_arr=[]
for i in range(len(data)):
	x_arr.append(data[i][0])
	y_arr.append(data[i][1])
def lsfit(x,y):
	Ex,Ey,Exx,Exy=0,0,0,0
	

	for i in range(len(x)):
		Ex+=x[i]
		Ey+=y[i]
		Exx+=(x[i]**2)
		Exy+=(x[i]*y_arr[i])
	

	Ex,Ey,Exx,Exy=(Ex/len(x)),(Ey/len(x)),(Exx/len(x)),(Exy/len(x))
	m=(Exy-Ex*Ey)/(Exx-Ex**2)
	c=(Exx*Ey-Ex*Exy)/(Exx-Ex**2)
	return m,c

m,c=lsfit(x_arr,y_arr)
yfit=[(m*x+c) for x in x_arr]

#planck's constant from expt
el=1.602e-19
h=m*el
#planck's constant from wiki
h1=6.62607015e-34
err=(h1-h)*100/h1
f=open('output.txt','w')
f.write('m='+str(m)+'\nc='+str(c)+'\nh (from millikans data)='+str(h)+'\nh (from wiki)='+str(h1)+'\nerror='+str(err)+'%')
f.close()

plt.scatter(x_arr,y_arr)
plt.savefig('scatter')


plt.plot(x_arr,yfit)
plt.savefig('fit')
plt.clf()