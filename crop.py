#crop 

import os 

import cv2 

img = cv2.imread(os.path.join('.', 'dogs'))

print(img.shape)

cropped_img = img[110:300, 100:500]
cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)
