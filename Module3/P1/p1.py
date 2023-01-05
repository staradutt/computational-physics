

def fact_int(n):
	temp=1
	for i in range(1,n+1):
		temp*=i
	return temp
def fact_float(n):
	temp=1.0
	for i in range(1,n+1):
		temp*=i
	return temp
f=open('out.txt','w')
f.write('factorial of 200 using integer variable is '+str(fact_int(200)))
f.write('.\n\nfactorial of 200 using floating point variable is '+str(fact_float(200)))
f.write(""".\nIntegers in python are stored exactly, this is done by stitching/joining of bytes whereas 
floating point numbers have size restriction due to bit representation and hence have upper and lower limits.""")
f.close()