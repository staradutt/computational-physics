

a1 = 15.67
a2 = 17.23
a3 = 0.75
a4 = 93.2

#function to evaluate a5 for given (A,Z)
def a5(A,Z):
	if (A%2)==1:
		return 0
	else:
		if(Z%2)==0:
			return 12
		if(Z%2)==1:
			return -12


#function to calculate binding energy
def BE(A,Z):
	B=(a1*A) - (a2*(A**(2/3))) - (a3*(Z**2)/(A**(1/3))) - (a4*((A-2*Z)**2)/A) + (a5(A,Z)/(A**(0.5)))
	return B
#function to give Binding Energy per Nucleon
def BPN(A,Z):
	return(BE(A,Z)/A)
#function to find most stable A for given Z
def MostStable_A(Z):
	maxi=Z
	
	for i in range(Z,3*Z+1):
		if BPN(i,Z)>=BPN(maxi,Z):
			
			maxi=i
	return maxi,BPN(maxi,Z)
k1=[] #to store Z
k2=[] #to store most stable A
k3=[] #to store BPN
for Z in range(1,101):
	k1.append(Z)
	k2.append(MostStable_A(Z)[0])
	k3.append(MostStable_A(Z)[1])
Btemp=BPN(1,1)
max_index=0
for i in range(len(k3)):
	if k3[i]>=Btemp:
		max_index=i
		Btemp=k3[i]

f=open('output','w')
f.write('Binding Energy of (A=58,Z=28) = '+str(BE(58,28)))
f.write('\nBinding Energy per nucleon of (A=58,Z=28) = '+str(BPN(58,28))+'\n')
f.write('Z , most stable A , BE\n' )
for i in range(len(k3)):
	f.write(str(k1[i])+' , '+str(k2[i])+' , '+str(k3[i])+'\n' )
f.write('most stable Z = '+str(k1[max_index])+'\ncorresponding A = '+ str(k2[max_index])+'\ncorresponding BE per nucleon = '+ str(k3[max_index])  )
f.close()