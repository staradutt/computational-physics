from math import pi
G = 6.67408e-11
Msun=1.989e30
cf=1/(3600*24)#conversion factor second to day
lin = float(input('Enter perihelion distance (l1) in m: '))
vin = float(input('Enter velocity at perihelion (v1) in m/s): '))
#function to give orbital parameters
def orb_params(l1,v1):
	l2=1/((2*G*Msun /((v1**2)*(l1**2)))-(1/l1))
	v2=(l1*v1)/l2
	a=(l2+l1)/2
	T=2*pi*((1/(G*Msun))**0.5)*(a**1.5)*cf
	e=(v1-v2)/(v1+v2)
	return l2,v2,T,e
earth_params = orb_params(1.4710e11, 3.0287e4)
halley_params=orb_params(8.7830e10, 5.4529e4)
user_params=orb_params(lin,vin)

f=open('output','w')
f.write('\nEarth\n\n')
f.write('Aphelion distance(l2) = '+str(earth_params[0])+'m\n')
f.write('Aphelion velocity(v2) = '+str(earth_params[1])+'m/s\n')
f.write('Time Period = '+str(earth_params[2])+'days\n')
f.write('Eccentricity = '+str(earth_params[3])+'\n')

f.write('\nHalley\n\n')
f.write('Aphelion distance(l2) = '+str(halley_params[0])+'m\n')
f.write('Aphelion velocity(v2) = '+str(halley_params[1])+'m/s\n')
f.write('Time Period = '+str(halley_params[2])+'days = '+str(halley_params[2]/365)+'earth years \n')
f.write('Eccentricity = '+str(halley_params[3])+'\n')

f.write('\nUser Input\n\n')
f.write('Aphelion distance(l2) = '+str(user_params[0])+'m\n')
f.write('Aphelion velocity(v2) = '+str(user_params[1])+'m/s\n')
f.write('Time Period = '+str(user_params[2])+'days \n')
f.write('Eccentricity = '+str(user_params[3])+'\n')