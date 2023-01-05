import numpy as np 
from random import random,choice
from math import e 
from matplotlib import pyplot as plt 


def E(dimer_arr):
	return -(len(dimer_arr))
def neighbour(site):
	n_arr=[]
	if site[0]+1<L:
		n_arr.append([site[0]+1,site[1]])
	if site[0]-1>-1:
		n_arr.append([site[0]-1,site[1]])
	if site[1]+1<L:
		n_arr.append([site[0],site[1]+1])
	if site[1]-1>-1:
		n_arr.append([site[0],site[1]-1])
	return n_arr
def exp_cool(T):
	return T*e**(-1/cooling_const)
def one_step_mc(dimer_arr):
	rnd_site=[choice(range(L)),choice(range(L))]
	rnd_dimer=[rnd_site,choice(neighbour(rnd_site))]
	rnd_dimer.sort()

	if rnd_dimer in dimer_arr:
		dimer_arr.remove(rnd_dimer)
	else:
		flag=1
		for dim in dimer_arr:
			if (rnd_dimer[0] in dim) or (rnd_dimer[1] in dim):
				flag=0
				break
		if flag==1:
			dimer_arr.append(rnd_dimer)
def sim_anneal(T,dimer_arr):
	dim_arr_copy=[i for i in dimer_arr]
	one_step_mc(dim_arr_copy)
	Eini=E(dimer_arr)
	Efin=E(dim_arr_copy)
	if Efin<Eini:
		dimer_arr=dim_arr_copy
	else:
		p=e**(-(Efin - Eini)/T)
		if random()<p:
			dimer_arr=dim_arr_copy
	return(dimer_arr)
def plot_dimers(dimer_arr):
	for dim in dimer_arr:
		plt.plot([dim[0][0],dim[1][0]],[dim[0][1],dim[1][1]],'lightcoral')
#for L=50 slow cool
cooling_const=10000
L=50
T=1
dimer_list=[]


while T>1e-2:
	
	dimer_list=sim_anneal(T,dimer_list)

	T=exp_cool(T)
	
plt.xlim(-1, L)
plt.ylim(-1, L)
plt.axis("off")
plot_dimers(dimer_list)
plt.title('slow cool L=50, \u03c4 = 10000, # of dimers = '+str(len(dimer_list)))
plt.savefig('slowcool.png')
plt.close()
		
#for L=50 fast cool
cooling_const=100
L=50
T=1
dimer_list=[]


while T>1e-2:
	
	dimer_list=sim_anneal(T,dimer_list)

	T=exp_cool(T)
	
plt.xlim(-1, L)
plt.ylim(-1, L)
plt.axis("off")
plot_dimers(dimer_list)
plt.title('fast cool L=50, \u03c4 = 100, # of dimers = '+str(len(dimer_list)))
plt.savefig('fastcool.png')
plt.close()

#L=10,tau=1000 for animation
cooling_const=1000
L=10
T=1
dimer_list=[]

i=0
while T>1e-2:
	l1=len(dimer_list)
	dimer_list=sim_anneal(T,dimer_list)

	T=exp_cool(T)
	l2=len(dimer_list)
	if l1!=l2:
		plt.xlim(-1, L)
		plt.ylim(-1, L)
		plt.axis("off")
		plot_dimers(dimer_list)
		plt.title('L=10, \u03c4 = 1000, T = '+str(round(T,3)))
		plt.savefig('frame/dim'+str(i)+'.png')
		plt.close()
		i+=1




