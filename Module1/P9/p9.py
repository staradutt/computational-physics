from math import sqrt,ceil
#function that returns 1 if number is prime
print
def prime(n):
	for i in range(2,ceil(sqrt(n))+1):
		if (n%i)==0:
			return 0
			break
	return 1
f=open('output','w')
f.write('list of primes < 10000 :\n')
prime_arr=[2]
for i in range(3,10000):
	if prime(i)==1:
		prime_arr.append(i)
f.write(str(prime_arr))
f.close()