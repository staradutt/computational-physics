from math import sqrt 
def qsolve1(a,b,c):
	sol=[]
	sol.append((-b+sqrt(b**2-4*a*c))/(2*a))
	sol.append((-b-sqrt(b**2-4*a*c))/(2*a))
	return sol
def qsolve2(a,b,c):
	sol=[]
	sol.append((2*c)/(-b-sqrt(b**2-4*a*c)))
	sol.append((2*c)/(-b+sqrt(b**2-4*a*c)))
	return sol
def qsolve3(a,b,c):
	sol=[]
	if (b>0):
		sol.append((2*c)/(-b-sqrt(b**2-4*a*c)))
		sol.append((-b-sqrt(b**2-4*a*c))/(2*a)) 
	else:
		sol.append((-b+sqrt(b**2-4*a*c))/(2*a))
		sol.append((2*c)/(-b+sqrt(b**2-4*a*c)))
	return sol
a=int(input('Enter a :   '))
b=int(input('Enter b :   '))
c=int(input('Enter c :   '))
f=open('out.txt','w')
f.write('solution of 0.001(x^2)+1000x+0.001 by first method is :'+str(qsolve1(0.001,1000,0.001)))
f.write('.\nsolution of 0.001(x^2)+1000x+0.001 by second method is :'+str(qsolve2(0.001,1000,0.001)))
f.write("""\n\nWhen we subtract two closeby numbers we generate errors if the difference is close to
to machine precision. So the correct way is to select one root from each method so that the problem is avoided.\n""")
f.write('\nsolution of 0.001(x^2)+1000x+0.001 by correct method is :'+str(qsolve3(0.001,1000,0.001)))
f.close()
print('solution by 1st method:'+str(qsolve1(a,b,c)))
print('\n\nsolution by 2nd method:'+str(qsolve2(a,b,c)))
print('\n\nsolution by correct method:'+str(qsolve3(a,b,c)))
