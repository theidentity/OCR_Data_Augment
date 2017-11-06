import numpy as np
import cv2


def clip_vertical(img):
	vert_proj = np.sum(img,axis=1)
	points = np.where(vert_proj!=0)
	top_cut = points[0][0]
	bottom_cut = points[0][-1]
	img = img[top_cut:bottom_cut,:]
	return img

def clip_horizontal(img):
	hor_proj = np.sum(img,axis=0)
	points = np.where(hor_proj!=0)
	left_cut = points[0][0]
	right_cut = points[0][-1]
	img = img[:,left_cut:right_cut]
	return img

def clip_around_img(img):
	img = 255-img
	img = clip_horizontal(img)
	img = clip_vertical(img)
	img = 255-img
	return img

def threshold_img(img,threshold=127):
	img[img>threshold]=255
	img[img<=threshold]=0
	return img 
	
# img = cv2.imread('datasets/F015/00010.tif',0)
# out = clip(img)
# out = cv2.imwrite('out.jpg',out)
