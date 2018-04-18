import numpy as np
import cv2


textOrg = (50, 100)
image = np.zeros((400, 400))
cv2.putText(image, 'MISIS THE BEST?', textOrg, cv2.FONT_HERSHEY_SIMPLEX, 1., 200, 2, 9)
cv2.imshow("Hi MISIS!", image)
cv2.waitKey()
