
from numpy import pi,sin,cos,array,zeros,copy,sqrt
from random import choice,uniform
from matplotlib import pyplot as plt




def plot(L):

	centre = int((L-1)/2)
	def radius (x,y):
		rad=sqrt((x-centre)**2+(y-centre)**2)
		return rad 
	def hit_edge (A,i,j):
		if A[i+1,j]+A[i-1,j]+A[i,j+1]+A[i,j-1]!=0:
			return 1
		else:
			return 0
	def new (r,A):
		theta = uniform(0,2*pi)
		j=int(r*cos(theta))+centre
		i=int(r*sin(theta))+centre

		if A[i,j]!=0:
			return new(r,A)
		else:
			return array([i,j])
	direc_arr=[[0,1],[0,-1],[1,0],[-1,0]]
	pos_centre=array([centre,centre])
	pos=copy(pos_centre)
	pos_arr=zeros((L,L))
	pos_arr[centre,centre] = 1
	r=2
	pos=new(r,pos_arr)



	tstart=1000 
	cnt=tstart
	while (4*r)<L:
		if (hit_edge(pos_arr,pos[0],pos[1])):
			pos_arr[pos[0],pos[1]]=cnt
			r=radius(pos[0],pos[1])+1
			pos=new(r,pos_arr)
			pos_arr[pos[0],pos[1]]=cnt
		elif radius(pos[0],pos[1])>2*r:
			pos_arr[pos[0],pos[1]]=0
			pos=new(r,pos_arr)
			pos_arr[pos[0],pos[1]]=cnt
		else:
			pos_arr[pos[0],pos[1]]=0
			increment=array(choice(direc_arr))    
			pos=pos+increment
			pos_arr[pos[0],pos[1]]=cnt
		
		cnt+=1
	  

	plt.figure(figsize=(20,20))
	plt.axis('off')
	plt.imshow(pos_arr,cmap='Blues')
	plt.savefig('DLAc_L_'+str(L)+'.png')
	plt.show()
	plt.close()

plot(101)
plot(201)