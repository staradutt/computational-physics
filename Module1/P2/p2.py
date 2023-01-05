from function import radial
x=float(input('Enter X:'))
y=float(input('Enter Y:'))
r,theta=radial(x,y)
print('r=',r,'\ntheta=',theta,'\nresult file generated')

f=open('result','w')
f.write('X input= '+str(x)+'\n')
f.write('Y input= '+str(y)+'\n')
f.write('r= '+str(r)+'\ntheta= '+str(theta))
f.close()




