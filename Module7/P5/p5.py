import random

def vol_hypsph(N,d):
	count=0
	A=2**d
	for i in range(N):
		sqr=0
		for i in range(d):
			sqr+=(2*random.random()-1)**2
		if sqr<1:
			count+=1
	vol=count*A/N
	return vol		

print('Volume of 10 dimensional hypersphere = ',vol_hypsph(1000000,10))