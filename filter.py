import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

image = np.zeros((100, 100))
image = cv.imread('maxresdefault.jpg')

plt.imshow(image)
plt.show()
filtr = np.array([[-0.5, 0.5]])

res = cv.filter2D(image, -1, filtr)
plt.imshow(res)
plt.show()
