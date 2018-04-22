import cv2 as cv
import numpy as np

image = cv.imread('razmetka.jpg')
image2 = cv.imread('razmetka.jpg')

for i in range(9, len(image) - 9):
    for j in range(9, len(image[i]) - 9):
        if (image[i][j][0] < 90 and image[i][j][1] > 90 and image[i][j][2] > 90 and abs(image[i][j][2] - image[i][j][1]) < 100):
            print ("color {0} {1}".format(i, j))
            for x in range(-7, 8):
                for y in range(-7, 8):
                    image2[i + x][j + y] = [0, 0, 255]

cv.imshow("Hi road", image2)
cv.waitKey()
