import numpy as np 
from matplotlib import pyplot as plt 
from math import e 

def L1(arr1,arr2,itr,i):
	val=(np.sum([abs(arr2[i]-arr1[i]) for i in range(len(arr1))]))*(1/len(arr1))
	data[i+1].append(val)
	data[i].append(itr)

def rho(x,y):
	if x>=-0.3 and x<=0.3:
		return e**(-(y/0.1))
	else:
		return 0
def jacobi(a,b,N):
	
	x_arr=np.linspace(a,b,N)
	y_arr=np.flip(np.linspace(a,b,N))
	delta=x_arr[1]-x_arr[0]
	pot=[[rho(x,y) for x in x_arr] for y in y_arr]
	


	A=np.zeros((N,N))
	itr=0
	r1=[]
	s1=[]
	
	
	
	while itr<1001:
		
		
		if itr in [10,100,1000]:
			plt.contour(A)
			plt.colorbar()
			plt.title('iter = '+str(itr))
			plt.savefig('jacobi_'+str(itr)+'.png')
			plt.clf()
		
		Acopy=np.copy(A)
		for i in range(N):
			for j in range(N):
				p=i+1
				q=i-1
				r=j+1
				s=j-1
				if i==0:
					q=N-1
				if j==0:
					s=N-1
				if i==N-1:
					p=0
				if j==N-1:
					r=0
				A[i][j]=0.25*(Acopy[p][j]+Acopy[q][j]+Acopy[i][r]+Acopy[i][s])-0.25*pot[i][j]*delta**2
				if itr%2==0:
					r1.append(A[i][j])
				if itr%2==1:
					s1.append(A[i][j])		
		if itr%2==1:
			L1(r1,s1,itr-1,0)
			r1=[]
			s1=[]
		itr+=1
	return 0
def GS(a,b,N):
	
	x_arr=np.linspace(a,b,N)
	y_arr=np.flip(np.linspace(a,b,N))
	delta=x_arr[1]-x_arr[0]
	pot=[[rho(x,y) for x in x_arr] for y in y_arr]
	


	A=np.zeros((N,N))
	itr=0
	r1=[]
	s1=[]
	
	while itr<1001:
		
		if itr in [10,100,1000]:
			plt.contour(A)
			plt.colorbar()
			plt.title('iter = '+str(itr))
			plt.savefig('GS_'+str(itr)+'.png')
			plt.clf()
			
		
		for i in range(N):
			for j in range(N):
				p=i+1
				q=i-1
				r=j+1
				s=j-1
				if i==0:
					q=N-1
				if j==0:
					s=N-1
				if i==N-1:
					p=0
				if j==N-1:
					r=0
				A[i][j]=0.25*(A[p][j]+A[q][j]+A[i][r]+A[i][s])-0.25*pot[i][j]*delta**2
				if itr%2==0:
					r1.append(A[i][j])
				if itr%2==1:
					s1.append(A[i][j])		
		if itr%2==1:
			L1(r1,s1,itr-1,2)
			r1=[]
			s1=[]
					
		itr+=1
	return 0
def SOR(a,b,N,w):
	
	x_arr=np.linspace(a,b,N)
	y_arr=np.flip(np.linspace(a,b,N))
	delta=x_arr[1]-x_arr[0]
	pot=[[rho(x,y) for x in x_arr] for y in y_arr]
	


	A=np.zeros((N,N))
	itr=0
	r1=[]
	s1=[]
	

	while itr<1001:

		
		if itr in [10,100,1000]:
			plt.contour(A)
			plt.colorbar()
			plt.title('\u03C9 = '+str( w)+', iter = '+str(itr))
			plt.savefig('SOR_'+str(itr)+'_\u03C9_'+str(w)+'.png')

			plt.clf()
			
		for i in range(N):
			for j in range(N):
				p=i+1
				q=i-1
				r=j+1
				s=j-1
				if i==0:
					q=N-1
				if j==0:
					s=N-1
				if i==N-1:
					p=0
				if j==N-1:
					r=0
				A[i][j]=A[i][j]+w*((0.25*(A[p][j]+A[q][j]+A[i][r]+A[i][s])-0.25*pot[i][j]*delta**2)-A[i][j])
				if itr%2==0:
					r1.append(A[i][j])
				if itr%2==1:
					s1.append(A[i][j])		
		if itr%2==1:
			if w==0.5:
				L1(r1,s1,itr-1,4)
			if w==1.5:
				L1(r1,s1,itr-1,6)
			r1=[]
			s1=[]

		itr+=1
	return 0








data=[[],[],[],[],[],[],[],[]]
jacobi(-1,1,40)
GS(-1,1,40)
SOR(-1,1,40,0.5)
SOR(-1,1,40,1.5)


plt.plot(data[0],data[1])
plt.ylabel('L1 error ')
plt.xlabel('iteration')
plt.title('jacobi')
plt.savefig('JacobiL1vsIter.png')
plt.clf()

plt.plot(data[2],data[3])
plt.ylabel('L1 error ')
plt.xlabel('iteration')
plt.title('GS')
plt.savefig('GS_L1vsIter.png')
plt.clf()


plt.plot(data[4],data[5])
plt.ylabel('L1 error ')
plt.xlabel('iteration')
plt.title('SOR \u03C9=0.5')
plt.savefig('SOR\u03C9-0.5_L1vsIter.png')
plt.clf()

plt.plot(data[6],data[7])
plt.ylabel('L1 error ')
plt.xlabel('iteration')
plt.title('SOR \u03C9=1.5')
plt.savefig('SOR\u03C9-1.5_L1vsIter.png')
plt.clf()

