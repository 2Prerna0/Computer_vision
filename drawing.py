import os 

import cv2

img = cv2.imread(os.path.join('.','whiteboard.jpg'))

#line 
cv2.line(img, (100, 150), (300, 450), (0, 255, 0), 3)

#rectangle
cv2.rectangle(img, (200, 350), (450, 600), (0, 0, 255), 5)

#circle
cv2.circle(img, (300, 200), 75, (255, 0, 0), 5)

#text
cv2.putText(img, 'Hey You!', (300, 200), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 2)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()