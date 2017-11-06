import numpy as np
import cv2
from scipy.misc import imrotate,imresize
from scipy.ndimage import shift

img = cv2.imread('datasets/F015/00010.tif',0)
label = 'F015'

def random_shift_hor(img,left=0,right=0):
	shift_val = np.random.uniform(left,right)
	shift_img = shift(img,(0,shift_val),mode='constant',cval=255)
	return shift_img

def random_shift_ver(img,top=0,bottom=0):
	shift_val = np.random.uniform(top,bottom)
	shift_img = shift(img,(shift_val,0),mode='constant',cval=255)
	return shift_img

def random_shift(img,top=0,right=0,bottom=0,left=0):
	shift_val_hor = np.random.uniform(left,right)
	shift_val_vert = np.random.uniform(top,bottom)
	shift_img = shift(img,(shift_val_vert,shift_val_hor),mode='constant',cval=255)
	return shift_img

def random_rotation(img,lower=0,upper=0):
	angle = np.random.uniform(lower,upper)
	img = 255-img
	rot = imrotate(img,-angle)
	rot = 255-rot
	return rot

# out = random_shift_hor(img,-5,5)
# out = random_shift_ver(img,-5,5)
# out = random_shift(img,-5,-5,5,5)
# out = random_rotation(img,10,10)
cv2.imwrite('img.jpg',img)
cv2.imwrite('out.jpg',out)

