from math import sqrt,pi

#constants
G=6.67408e-11#univ grav const
Me=5.9722e24#mass of earth
Re=6378100#radius of earth


#function to calculate altitude given time period
def Alti(T):
	r=(T/(2*pi)*sqrt(G*Me))**(2.0/3.0)
	return r-Re
Tin=float(input('Enter T in s: '))


f=open('output','w')
f.write('part A\n\n')
f.write('Desired input revolution time for satellite in s = '+str(Tin)+'\n')
f.write('Calculated altitude in km= '+str(Alti(Tin)/1000)+'\n')
f.write('\npart B\n\n')
f.write('Altitude of satellite that orbit earth once every day: '+str((Alti(24*60*60))/1000) + ' km\n')
f.write('Altitude of satellite that orbit earth once every 90 min: '+str((Alti(90*60))/1000) + ' km\n')
f.write('Altitude of satellite that orbit earth once every 45 min: '+str((Alti(45*60))/1000) + ' km\n\n')
f.write('As altitude cannot be negative,it suggests that there is a minimum time period at which altitude is zero.')
f.write('\nThe satellite grazes the surface of earth in that case.\n\n')
f.write('part C\n\n')
f.write('Altitude of geosynchronous satellite:'+str((Alti(23.93*3600))/1000)+'km\n')
f.write('''The earth takes 23hrs56min i.e.23.93hrs to complete a rotation,but between two sunrise in a given place on earth 
the time is 24hr. This is because of revolution of earth for which it needs to rotate 4 more minutes to catch up with the sun.\n''')
f.write('Altitude difference: '+str(( Alti(24*3600) - Alti(23.93*3600))/1000)+'km\n'      )
f.close()
print('output file generated')