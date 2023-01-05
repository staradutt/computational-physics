a=1664525
c=1013904223
M=2147483648

seed=1011123

def rnd1to6():
	global seed
	seed=(a*seed+c)%M
	return(int(1+6*seed/(M-1)))
count=0
maxthrow=1000000
for i in range(maxthrow):
	t1=rnd1to6()
	t2=rnd1to6()
	if t1==6 and t2==6:
		count+=1


f=open('result.txt','w')
f.write('Actual probability of getting 2 sixes in a throw of double dice: '+str(round(1/36,6))+',')
f.write('\n\nProbability from running simulation for million throws: '+str(count/maxthrow)+'.')
f.close()
print('result saved in file named result.txt')