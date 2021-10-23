import cv2
import random

img = cv2.imread('assets/imagetest.jpg', 1)

#changing 100 first rows to random colors
#for i in range(100):
#	for j in range(img.shape[1]):
#		img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

#takes the pixels from 200 rows down and pastes them up top
for i in range(100):
	for j in range(img.shape[1]):
		img[i][j] = img[i+200][j]

		#rows 		collumns
#tag = img[200:350, 400:550]
#img[100:250, 300:450] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows

print(img[257][45:400])