import numpy as np
from random import choice
from matplotlib import pyplot as plt


L=201

centre=int((L-1)/2)

def edge_hit (A,i,j):
	if (i==0 or i==L-1 or j==0 or j==L-1):
		return 1
	

	elif (A[i+1,j]+A[i-1,j]+A[i,j+1]+A[i,j-1])!=0:
		return 1
	

	else:
		return 0

direc_arr=[[0,1],[0,-1],[1,0],[-1,0]]

pos_centre=np.array([centre,centre])

pos=np.copy(pos_centre)

pos_arr=np.zeros((L,L))
pos_arr[centre,centre]=1



t_start=1000 

count=t_start


while (edge_hit(pos_arr,pos_centre[0],pos_centre[1]) and pos_arr[pos_centre[0],pos_centre[1]])==0:
	
	if (edge_hit(pos_arr,pos[0],pos[1])):
		pos_arr[pos[0],pos[1]]=count
		pos=np.copy(pos_centre)
		pos_arr[pos[0],pos[1]]=count
	

	else:
		pos_arr[pos[0],pos[1]]=0
		increment=np.array(choice(direc_arr))    
		pos=pos+increment
		pos_arr[pos[0],pos[1]]=count
	
	
	count+=1
  


plt.figure(figsize=(20,20))

plt.imshow(pos_arr,cmap='Blues')
plt.axis('off')
plt.savefig('DLA201.png')
plt.show()
plt.close()

