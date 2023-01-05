import numpy as np 
from matplotlib import pyplot as plt 
import random 

def plot(L,N):
	d=(L-1)/2
	pos=[0,0]
	
	def pos_updater(i,pos):
		
		#up =0 down=1 left=2 right=3
		p=np.copy(pos)
		if i==0:
			p[1]+=1
		elif i==1:
			p[1]-=1
		elif i==2:
			p[0]-=1
		elif i==3:
			p[0]+=1

		return p[0],p[1]

	x_arr=[]
	y_arr=[]
	x_arr.append(pos[0])
	y_arr.append(pos[1])
	i=0

	while i < N:
		
		a,b=pos_updater(int(random.random()*4),pos)
		while (abs(a)>d or abs(b)>d):
			a,b=pos_updater(int(random.random()*4),pos)
			
		pos[0]=a
		pos[1]=b
		x_arr.append(a)
		y_arr.append(b)
		i+=1
		
	plt.plot(x_arr,y_arr)
	plt.xlim(-d,d)
	plt.ylim(-d,d)
	plt.title('2D random walk, L = '+str(L)+',steps = '+str(N))
	plt.xlabel('x')
	plt.ylabel('y')
	plt.savefig('L_'+str(L)+'&'+str(N)+'_steps''.png')
	plt.close()

plot(101,10000)
plot(101,100000)
plot(101,1000000)
plot(1001,1000000)



