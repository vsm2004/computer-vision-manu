import cv2
import numpy as np
image = cv2.imread('C:\\Users\\DELL\\Pictures\\srk pic don.jpg', cv2.IMREAD_GRAYSCALE)  # Replace 'path_to_image.jpg' with the actual image path
equalized_image = cv2.equalizeHist(image)
comparison = np.hstack((image, equalized_image))
cv2.imshow('Original Image vs. Equalized Image', comparison)
cv2.waitKey(0)
cv2.destroyAllWindows()
