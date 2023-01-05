
a=1
b=2
maxiter=100
f=open('out.txt','w')
def xfunc1(x,y):
	return y*(a+x**2)
def yfunc1(x,y):
	return b/(a+x**2)
def xfunc2(x,y):
	return ((b/y)-a)**0.5
def yfunc2(x,y):
	return x/(x**2+a)
def solve(f1,f2,guessx,guessy,tol):
	x=guessx
	y=guessy
	iter=0
	f.write('using modified forms\n')
	f.write('iter     x     y\n')
	f.write(str(iter)+'   '+str(x)+'  '+str(y)+'\n')

	while abs(f1(x,y)-x)>tol or abs(f2(x,y)-y)>tol:
		x=f1(x,y)
		y=f2(x,y)
		iter+=1
		f.write(str(iter)+'   '+str(x)+'  '+str(y)+'\n')
	f.write('Root(x,y)=   '+str(x)+'  '+str(y)+'\n')
	return x,y
sol1=solve(xfunc2,yfunc2,1,1,1e-10)
f.close()
