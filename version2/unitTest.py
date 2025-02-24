import re
import numpy as np
import cv2
#from picamera import PiCamera
from PIL import Image, ImageChops
import PIL
import matplotlib.pyplot as plt
import cv2

img = cv2.imread(f'assets/all80.jpg')#reading init pic
#cv2.imshow('window', img)
#cv2.waitKey()


def autoCoords():
	leftY = 468
	rightY = 480
	
	for index in range(0,80):
		column0 = img[260:650, leftY:rightY]
		plt.imsave(f"assets/testing{index}.jpg", column0)		

		leftY +=13
		rightY +=13
		if index == 0:
			continue


		if index % 5 == 0 and index % 20 != 0:
			print(index, "removing 4")
			leftY +=-4
			rightY +=-4

		if index % 30 == 0:
			print(index, "removing 8")
			leftY +=-8
			rightY +=-8

autoCoords()

def getCharacter(final):	
	if final > 20 and final < 50:
		selector = 0
		return selector
	elif final > 55 and final < 90:
		selector = 1
		return selector
	elif final > 95 and final < 120:
		selector = 2		
		return selector
	elif final > 125 and final < 151:
		selector = 3		
		return selector
	elif final > 151 and final < 180:
		selector = 4
		return selector
	elif final > 190 and final < 229:
		selector = 5
		return selector
	elif final > 230 and final < 255:
		selector = 6
		return selector
	elif final > 265 and final < 285:
		selector = 7
		return selector
	elif final > 295 and final < 320:
		selector = 8
		return selector
	elif final > 330 and final < 355:
		selector = 9
		return selector

	