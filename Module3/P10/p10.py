from math import e
V=5
R1=1e3
R2=4e3
R3=3e3
R4=2e3
I0=3e-9
VT=0.05

def compute(V1):
	V2=(V*((1/R1)+(1/R3))-V1*((1/R1)+(1/R2)))/((1/R3)+(1/R4))
	return (I0*(e**((V1-V2)/VT)-1)+((V1/R2)-((V-V1)/R1)))
def deriv(V1):
	V2=(V*((1/R1)+(1/R3))-V1*((1/R1)+(1/R2)))/((1/R3)+(1/R4))
	der= -((1/R1)+(1/R2))/((1/R3)+(1/R4))#derivative of v2 wrt v1
	return ((I0/VT)*(e**((V1-V2)/VT)))*(1-der)+((1/R2)+(1/R1))
def solve(f, d, guess, tol):
	x = guess
	while(abs(f(x))>tol):
		x-=(f(x)/d(x))
	return x

v1 = solve(compute, deriv, 4.5, 1e-17)
v2=(V*((1/R1)+(1/R3))-v1*((1/R1)+(1/R2)))/((1/R3)+(1/R4))
f=open('out.txt','w')
f.write("V1: "+str(v1)+" V\n")
f.write("V2: "+str(v2)+" V\n")
f.write("V1 - V2: "+str(v1-v2)+" V\n")
f.write("V1 and V2 differ by approximately 0.6 V. \n")
f.close()

