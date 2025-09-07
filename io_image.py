import os

import cv2

#read image
image_path = os.path.join('.','data','bullet.jpg')
img = cv2.imread(image_path)

#write image 
cv2.imwrite(os.path.join(',', 'data', 'bird_out.jpg'), img)

# visualiza image 
cv2.imshow('image', img)
cv2.waitKey(5000)


# or 

import os
import cv2

# Read image
image_path = os.path.join('.', 'data', 'bullet.jpg')
img = cv2.imread(image_path)

# Resize the image to 800x600
resized_img = cv2.resize(img, (800, 600))  # Width, Height

# Display the resized image
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)


