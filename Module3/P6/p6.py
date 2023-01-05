from math import e


h=6.62607004e-34
c=299792458
kb=1.38064852e-23
z=(h*c)/kb#hc/kb is stored as z for convenience

def deriv(x):
	#x=w*T
	return (z/5)*((e**(z/x))/(e**(z/x)-1))-x
def solve_bisect(func,start,end,tol):
	a=start
	b=end
	c=(a+b)/2
	if func(a)*func(b)>0:
		print ('outside range ',a,b)
		return None
	while(abs(func(c))>tol):
		if (func(c)*func(a))>0:
			a=c
		else:
			b=c
		c=(a+b)*0.5
	return c
f=open('out.txt','w')
b=solve_bisect(deriv, 2e-3, 4e-3, 1e-16)
f.write("Part a\nWien's const= " + str(b) + " m K\n")
temp = b / (502e-9)
f.write("Part b\nTemp. of the Sun= " + str(temp) + " K\n")
f.close()
