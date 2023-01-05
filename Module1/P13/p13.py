import numpy as np

from matplotlib import pyplot as plt 



#creating image array from text file
img_arr=np.loadtxt('stm.txt')


#plotting image array
#converging colormap better boundaries
plt.imshow(img_arr,cmap='twilight')


plt.savefig('stm_img1')
plt.clf()
#diverging colormap for better interiors
plt.imshow(img_arr,cmap='seismic')


plt.savefig('stm_img2')
plt.clf()

