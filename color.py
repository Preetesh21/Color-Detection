#FEDORA PROJECT

import numpy as np
from urllib.request import urlopen
import cv2

url = 'https://resize.hswstatic.com/w_907/gif/color-box.jpg'
resp = urlopen(url)
img = np.asarray(bytearray(resp.read()), dtype="uint8")
img = cv2.imdecode(img, cv2.IMREAD_COLOR)

# blue color range
blue_low=np.array([136, 51, 4]) 
blue_high=np.array([220, 88, 50])

# red color range
# red_low=np.array([155,25,0]) 
# red_high=np.array([179,255,255])

# yellow color range
# yellow_low=np.array([25, 146, 190])
# yellow_high=np.array([62, 174, 250])

# detecting colors in images
image_mask=cv2.inRange(img,blue_low,blue_high)
out=cv2.bitwise_and(img,img,mask=image_mask)
cv2.imshow('BLUE',out)
cv2.waitKey(0)

# image_mask2=cv2.inRange(img1,red_low,red_high)
# out2=cv2.bitwise_and(img1,img1,mask=image_mask2)
# cv2.imshow('RED',out2)
# cv2.waitKey(0)

# image_mask3=cv2.inRange(img2,yellow_low,yellow_high)
# out3=cv2.bitwise_and(img2,img2,mask=image_mask3)
# cv2.imshow('YELLOW',out3)
# cv2.waitKey(0)
cv2.destroyAllWindows()
