import time
t=time.time()
c=1
for i in range(100):
	c=int(c*((4*i+2)/(i+2)))
t1=time.time()-t

print ('C100 = ',c)
print('time taken to calculate C100 = ',t1,'s')
print('output file generated')
f=open('output','w')
f.write('C100 = '+str(c)+'\ntime taken to calculate C100 = '+str(t1)+'s')
f.close()