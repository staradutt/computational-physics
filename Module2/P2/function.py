from math import sin,cos,pi
def func(m,x,t):
	r=cos(m*t-x*sin(t))
	return r
def J(m,x):
	N=1000
	h=pi/N
	I=func(m,x,0)+func(m,x,pi)
	for i in range(1,N//2):
		I=I+4*func(m,x,(2*i-1)*h)+2*func(m,x,2*i*h)
	I=(I*h)/(3*pi)
	return I