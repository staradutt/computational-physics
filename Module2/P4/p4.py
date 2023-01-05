from math import exp,pi
from gaussxw import gaussxwab


upperlim=100
def integrand(x):
	return x**3/(exp(x)-1)

def integral(N,a,b):
	x,w=gaussxwab(N,a,b)
	integral=0
	for i in range(len(x)):
		integral+=integrand(x[i])*w[i]
	return integral
def error(upperlim):
#error is got by approximating ( e^x-1) as e^x and then integrating analytically from upperlim to infinity
	analytical_error=(upperlim**3+3*upperlim**2+6*upperlim+6)/exp(upperlim)
	return analytical_error
integralval=integral(100,0,upperlim)+error(upperlim)
hbar = (6.62607015e-34)/(2*pi)
kb = 1.38064852e-23
c = 299792458
stefans_const = (((kb / hbar) ** 3) * kb) / (4 * ((pi * c) ** 2)) * integralval
f=open('out.txt','w')
f.write('stefans constant calculated by the program = '+str(stefans_const))
f.write('\nwikipedia value = 5.670367e-8, indicating  '+str(abs(stefans_const)*100/5.670367e-8)+'%  agreement')
f.write('\nanalytical error:\nvalue of integral approximated analytically from upper limit(1000) to +inf = ' +str(error(upperlim)))

f.close()
