from math import sqrt

mpow=1e-31
m=9.11e-31
E=10e-19
V=9e-19

h=6.62607004e-34

k1=sqrt(2*m*E)*(1/h)
k2=sqrt(2*m*(E-V))*(1/h)

#separating fractions and multiplying to avoid under/over flow
T=4*(k1/(k1+k2))*(k2/(k1+k2))
R=((k1-k2)/(k1+k2))**2

print('transmission probability = ',T,'\nreflecion probability = ',R)
f=open('output','w')
f.write('transmission probability = '+str(T))
f.write('\nreflecion probability = '+str(R))
f.close()
