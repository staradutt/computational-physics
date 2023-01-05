from matplotlib import pyplot as plt
from random import choice,random
from math import e

N=20
J=1

def NNperiodic(i,j):
	n_arr=[((i-1)%N,j),(i,(j-1)%N),((i+1)%N,j),(i,(j+1)%N)]
	return n_arr

def totalenergy(state):
	n=len(state)    
	E=0
	for i in range(n):
		for j in range(n):
			for nbr in NNperiodic(i,j):
				E+=J*state[i][j]*state[nbr[0]][nbr[1]]
	return E/2
def magnetisation(state):
	n=len(state)
	m=0
	for i in range(n):
		for j in range(n):
			m+=state[i][j]
	return m/(n**2)
def mc(state, T):
	beta=1/T
	n=len(state)
	switch=(choice(range(n)), choice(range(n)))
	nbr_arr=NNperiodic(switch[0], switch[1])
	delta_E=0
	
	for nbr in nbr_arr:
		delta_E+=2*J*state[nbr[0]][nbr[1]]*state[switch[0]][switch[1]]
	if delta_E<0:
		state[switch[0]][switch[1]]*=-1
	elif random()<=e**(-beta*delta_E):
		state[switch[0]][switch[1]]*=-1
	return state

def plot(T):
	rnd_state = [[choice([1,-1]) for i in range(N)] for j in range(N)]
	print('\ncalculating for T ='+str(T))
	x_arr=[]
	m_arr=[]
	for i in range(1000000):
		mc(rnd_state, T)
		x_arr.append(i)
		m_arr.append(magnetisation(rnd_state))

	plt.imshow(rnd_state,vmin=-1,vmax=1)
	plt.colorbar()
	plt.savefig('final_state for T = '+str(T))
	plt.close()
	plt.plot(x_arr,m_arr)
	plt.savefig('T_'+str(T)+'.png')
	plt.close()
	print('\nplot for T ='+str(T)+'saved.')
for t in [1,2,3]:
	plot(t)