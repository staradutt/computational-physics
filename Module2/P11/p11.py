import numpy as np 
from math import sin, cos, pi
from matplotlib import pyplot as plt 

def partialy(f, pos, h):

    N = len(f)
    return (f[(pos[0] + 1) % N][pos[1]] - f[(pos[0] - 1) % N][pos[1]]) / (2 * h)

def partialx(f, pos, h):

    N = len(f[0])
    return (f[pos[0]][(pos[1] + 1) % N] - f[pos[0]][(pos[1] - 1) % N]) / (2 * h)


data = np.loadtxt("altitude.txt")

deriv = []


for i in range(len(data)):
    row = []
    for j in range(len(data[0])):
        row.append((partialx(data, (i, j), 30000), partialy(data, (i, j), 30000)))
    deriv.append(row)
    

def Intensity(deriv_x, deriv_y, phi):

    return (cos(phi) * deriv_x + sin(phi) * deriv_y) / ((deriv_x ** 2 + deriv_y ** 2 + 1) ** 0.5)

grid = [[Intensity(deriv[i][j][0], deriv[i][j][1], pi / 4) for j in range(len(deriv[0]))] for i in range(len(deriv))]

plt.imshow(grid,cmap='gray')
plt.axis("off")
plt.savefig("relief_world_map.png")
plt.clf()


data2 = np.loadtxt("stm.txt")

deriv_2 = []
for i in range(len(data2)):
    row = []
    for j in range(len(data2[0])):
        row.append((partialx(data2, (i, j), 2.5), partialy(data2, (i, j), 2.5)))
    deriv_2.append(row) 

grid2 = [[Intensity(deriv_2[i][j][0], deriv_2[i][j][1], pi / 4) for j in range(len(deriv_2[0]))] for i in range(len(deriv_2))]

plt.imshow(grid2, cmap = "gray")
plt.axis("off")
plt.savefig("silicon.png")


