
def binomial(n,k):
	if k==0:
		return 1
	bn=1
	for i in range(k):
		bn=( bn * (n-i) / (i+1) )
		bn=round(bn)
	return bn

f=open('output','w')
f.write('part A\n\nThe binomial function is written in the program\n\npart B(Pascal\'s Triangle)\n\n')
N=20
for i in range(1,N+1):
	for j in range(i+1):
		f.write(str(binomial(i,j))+' ')
	f.write('\n')


def prob(n,k):
	return (binomial(n,k)/(2**n))

p1=prob(100,60)
p2=0
for i in range(60,100+1):
	p2+=prob(100,i)
f.write('\n\nPart C\n\nP(number of heads in 100 tosses = 60)= '+str(p1))
f.write('\nP(number of heads in 100 tosses > 60)= '+str(p2))
f.close()