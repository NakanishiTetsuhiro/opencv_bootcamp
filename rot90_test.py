import cv2
import matplotlib.pyplot as plt
import numpy as np
import os, sys

image = np.array( cv2.imread('buttle.jpg') )
plt.imshow(image,cmap='gray')
image = np.array(np.rot90(image,3) ) # put it right side up

image = image.copy() # Change

plt.imshow(image,cmap='gray')
cv2.rectangle(image,(0,0),(100,100),(255,0,0),2)
plt.imshow(image,cmap='gray')

plt.show() # Show image
