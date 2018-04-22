import cv2 as cv
import numpy as np

image = cv.imread('razmetka.jpg')
image2 = cv.imread('razmetka.jpg')

def check(val, max_val):
    return val >= 0 and val < max_val


for i in range(0, len(image)):
    for j in range(0, len(image[i])):
        if (image[i][j][0] < 100 and image[i][j][1] > 120 and image[i][j][2] > 120 and abs(image[i][j][2] - image[i][j][1]) < 50):
            print ("cord {}".format((i, j)))
            for x in range(-3, 4):
                for y in range(-3, 4):
                    if check(i + x, len(image)) and check(j + y, len(image[i])):
                        image2[i + x][j + y] = [0, 0, 255]

cv.imshow("Hi road", image2)
cv.waitKey()
