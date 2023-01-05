import random
from math import pi,acos

a=random.random()
b=random.random()
phi=2*pi*a
theta=acos(1-2*b)
print('random (\u0398,\u03d5) = ',(theta,phi))