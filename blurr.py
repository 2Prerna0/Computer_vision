import os 

import cv2

img = cv2.imread(os.path.join('.', 'dogs'))

k_size = 7
img_blur = cv2.blur(img, (k_size, k_size))
img_gussian_blur = cv2.GaussianBlur(img, (k_size, k_size),5)
img_median_blur = cv2.medianBlur(img, k_size)

cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gussian_blur', img_gussian_blur)
cv2.imshow('img_median_blur', img_median_blur)
cv2.waitKey(0)