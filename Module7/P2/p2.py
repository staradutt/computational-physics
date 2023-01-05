from matplotlib import pyplot as plt
import random

bi_213,tl_209,pb_209,bi_209=10000,0,0,0
t_bi_213,t_tl_209,t_pb_209=46*60,2.2*60,3.3*60

bi_213_arr=[bi_213]
tl_209_arr=[tl_209]
pb_209_arr=[pb_209]
bi_209_arr=[bi_209]
t_arr=[0]



s=0
T=20000
while s<T:
	s+=1
	t=1
	for i in range(pb_209):
		p1=random.random()
		p1_decay=1-2**(-t/t_pb_209)
		
		if p1 < p1_decay:
			pb_209-=1
			bi_209+=1

	for i in range(tl_209):
		p2=random.random()
		p2_decay=1-2**(-t/t_tl_209)
		
		if p2<p2_decay:
			pb_209+=1
			tl_209-=1

	for i in range(bi_213):
		p3=random.random()
		p3_decay=1-2**(-t/t_bi_213)
		
		if p3<p3_decay:
			bi_213-=1
			p=random.random()
			
			if p<0.9791:
				pb_209+=1
			
			else:
				tl_209+=1
	tl_209_arr.append(tl_209)
	bi_213_arr.append(bi_213)	
	pb_209_arr.append(pb_209)
	bi_209_arr.append(bi_209)
	t_arr.append(s)
plt.plot(t_arr,bi_213_arr,label="Bi_213")
plt.plot(t_arr,tl_209_arr,label="Tl_209")
plt.plot(t_arr,pb_209_arr,label="Pb_209")
plt.plot(t_arr,bi_209_arr,label="Bi_209")

plt.xlabel('t (s)')
plt.ylabel('# of atoms')


plt.legend()
plt.savefig('decay.png')
plt.show()
plt.close()



