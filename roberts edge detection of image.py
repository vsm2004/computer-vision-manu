import cv2
import numpy as np
from matplotlib import pyplot as plt

def roberts_edge_detection(image_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    if image is None:
        print("Could not open or find the image.")
        return
    
    # Define the Roberts Cross kernels
    kernel_x = np.array([[1, 0], [0, -1]], dtype=int)
    kernel_y = np.array([[0, 1], [-1, 0]], dtype=int)
    
    # Apply the Roberts kernels to the image using cv2.filter2D
    roberts_x = cv2.filter2D(image, -1, kernel_x)
    roberts_y = cv2.filter2D(image, -1, kernel_y)
    
    # Calculate the gradient magnitude (combine the two directions)
    roberts_combined = cv2.addWeighted(cv2.convertScaleAbs(roberts_x), 0.5, cv2.convertScaleAbs(roberts_y), 0.5, 0)
    
    # Display the images
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 2, 1), plt.imshow(image, cmap='gray')
    plt.title('Original Image'), plt.axis('off')
    plt.subplot(2, 2, 2), plt.imshow(roberts_x, cmap='gray')
    plt.title('Roberts X'), plt.axis('off')
    plt.subplot(2, 2, 3), plt.imshow(roberts_y, cmap='gray')
    plt.title('Roberts Y'), plt.axis('off')
    plt.subplot(2, 2, 4), plt.imshow(roberts_combined, cmap='gray')
    plt.title('Roberts Combined'), plt.axis('off')
    
    plt.show()

# Usage example: Provide the path to your image
roberts_edge_detection("C:\\Users\\DELL\\Pictures\\rani and srk.jpg")
