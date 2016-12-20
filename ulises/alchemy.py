import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

img=mpimg.imread('alchemy.png')

lun_img=img(:,:,0)

img2=plt.imshow(lum_img,cmap='hot')
img2.set_cmap('spectral')
plt.imshow(img2)

plt.hist(lum_img.ravel(),bins=256,range=(0.0,1.0))

plt.colorbar()
