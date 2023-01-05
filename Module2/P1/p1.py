from matplotlib import pyplot as plt
f=open('output.txt','w')
file = open("velocities.txt", 'r')
t_arr = []
v_arr = []
for line in file.readlines():
    point = line.split()
    t_arr.append(float(point[0]))
    v_arr.append(float(point[1]))
dist_arr=[0]
dist=0
f.write('time     distance\n')
f.write(str(t_arr[0])+'    '+str(0)+'\n')
#trapezoidal rule ..
for i in range(len(t_arr)-1):
	dist+=0.5*(t_arr[i+1]-t_arr[i])*(v_arr[i+1]+v_arr[i])
	dist_arr.append(dist)
	f.write(str(t_arr[i+1])+'    '+str(dist)+'\n')

f.close()


plt.plot(t_arr,dist_arr,label='distance')
plt.plot(t_arr,v_arr,label='velocity')
plt.legend()
plt.savefig('plot1.png')
plt.clf()

