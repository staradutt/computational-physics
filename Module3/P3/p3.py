def derivative(func,x,delta):
	deriv=(func(x+delta)-func(x))/delta
	return deriv
def quadf(x):
	return x*(x-1)

f=open('out.txt','w')
f.write('analytical derivative for function x*(x-1) at x=1 is 2*1-1 i.e. 1.')
f.write('\nderivative computed using delta = 10^(-2) is '+str(derivative(quadf,1,1e-2))+',accuracy = '+str(100*abs(derivative(quadf,1,1e-2))-1)+'%')
f.write('\nderivative computed using delta = 10^(-4) is '+str(derivative(quadf,1,1e-4))+',accuracy = '+str(100*abs(derivative(quadf,1,1e-4))-1)+'%')
f.write('\nderivative computed using delta = 10^(-6) is '+str(derivative(quadf,1,1e-6))+',accuracy = '+str(100*abs(derivative(quadf,1,1e-6))-1)+'%')
f.write('\nderivative computed using delta = 10^(-8) is '+str(derivative(quadf,1,1e-8))+',accuracy = '+str(100*abs(derivative(quadf,1,1e-8))-1)+'%')
f.write('\nderivative computed using delta = 10^(-10) is '+str(derivative(quadf,1,1e-10))+',accuracy = '+str(100*abs(derivative(quadf,1,1e-10))-1)+'%')
f.write('\nderivative computed using delta = 10^(-12) is '+str(derivative(quadf,1,1e-12))+',accuracy = '+str(100*abs(derivative(quadf,1,1e-12))-1)+'%')
f.close()
