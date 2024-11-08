import cv2
import numpy as np
from matplotlib import pyplot as plt

def sobel_edge_detection(image_path):
    # Read the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
    # Check if the image is loaded correctly
    if image is None:
        print("Could not open or find the image.")
        return
    
    # Apply Sobel edge detection in the X direction
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    
    # Apply Sobel edge detection in the Y direction
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
    
    # Convert the result back to an 8-bit unsigned integer
    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)
    
    # Combine the two directions
    sobel_combined = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
    
    # Plot the results
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 2, 1), plt.imshow(image, cmap='gray')
    plt.title('Original Image'), plt.axis('off')
    plt.subplot(2, 2, 2), plt.imshow(sobel_x, cmap='gray')
    plt.title('Sobel X'), plt.axis('off')
    plt.subplot(2, 2, 3), plt.imshow(sobel_y, cmap='gray')
    plt.title('Sobel Y'), plt.axis('off')
    plt.subplot(2, 2, 4), plt.imshow(sobel_combined, cmap='gray')
    plt.title('Sobel Combined'), plt.axis('off')
    
    plt.show()

# Usage example: Provide the path to your image
sobel_edge_detection("C:\\Users\\DELL\\Pictures\\rani and srk.jpg")
