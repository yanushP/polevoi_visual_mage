import numpy as np
import cv2
import matplotlib.pyplot as plt
import math

method = 2

white = (255,255,255)
black = (0,0,0)
gray = (128,128,128)

canvas = np.zeros((600,300,3), dtype=np.uint8)

cv2.rectangle(canvas,(0,0),(100,100),white,-1)
cv2.rectangle(canvas,(0,100),(100,200),white,-1)
cv2.rectangle(canvas,(0,200),(100,300),white,-1)

cv2.rectangle(canvas,(0,300),(100,400),white,-1)
cv2.rectangle(canvas,(0,400),(100,500),white,-1)
cv2.rectangle(canvas,(0,500),(100,600),white,-1)


cv2.rectangle(canvas,(100,0),(200,100),gray,-1)
cv2.rectangle(canvas,(100,100),(200,200),gray,-1)
cv2.rectangle(canvas,(100,200),(200,300),gray,-1)

cv2.rectangle(canvas,(100,300),(200,400),gray,-1)
cv2.rectangle(canvas,(100,400),(200,500),gray,-1)
cv2.rectangle(canvas,(100,500),(200,600),gray,-1)


cv2.circle(canvas,(50,50),25,black,-1)
cv2.rectangle(canvas,(25,125),(75,175),black,-1)
a3 = np.array( [[[25,225],[25,275],[75,275]]], dtype=np.int32 )
cv2.fillPoly(canvas, a3,black)

cv2.circle(canvas,(50,350),25,gray,-1)
cv2.rectangle(canvas,(25,425),(75,475),gray,-1)
a3 = np.array( [[[25,525],[25,575],[75,575]]], dtype=np.int32 )
cv2.fillPoly(canvas, a3,gray)

cv2.rectangle(canvas,(125,125),(175,175),black,-1)
cv2.circle(canvas,(150,50),25,black,-1)
a3 = np.array( [[[125,225],[125,275],[175,275]]], dtype=np.int32 )
cv2.fillPoly(canvas, a3,black)

cv2.rectangle(canvas,(125,425),(175,475),white,-1)
cv2.circle(canvas,(150,350),25,white,-1)
a3 = np.array( [[[125,525],[125,575],[175,575]]], dtype=np.int32 )
cv2.fillPoly(canvas, a3,white)

cv2.circle(canvas,(250,50),25,white,-1)
cv2.rectangle(canvas,(225,125),(275,175),white,-1)
a3 = np.array( [[[225,225],[225,275],[275,275]]], dtype=np.int32 )
cv2.fillPoly(canvas, a3,white)

cv2.circle(canvas,(250,350),25,gray,-1)
cv2.rectangle(canvas,(225,425),(275,475),gray,-1)
a3 = np.array( [[[225,525],[225,575],[275,575]]], dtype=np.int32 )
cv2.fillPoly(canvas, a3,gray)

canvas = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)

plt.imshow(canvas)
plt.show()
