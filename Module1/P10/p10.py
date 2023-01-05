import time
def catalan(n):
	if n==1:
		return 1
	return int((4*n-2)/(n+1)*catalan(int(n-1)))
def gcd(m,n):
	if n==0:
		return m
	elif n>0:
	
		return gcd(n,m%n)

t=time.time()
C100=catalan(100)
t1=time.time()-t
print ('C100 = ',C100)
print('time taken to calculate C100 = ',t1,'s')
temp=gcd(108,192)
print('gcd(108,192) = ',temp)

f=open('output','w')
f.write('C100 = '+str(C100)+'\ntime taken to calculate C100 = '+str(t1)+'s\nGCD(108,192) = '+str(temp))
f.close()