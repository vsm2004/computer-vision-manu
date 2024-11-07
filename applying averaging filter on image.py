import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_averaging_filter(image_path, kernel_size=(5, 5)):
    # Load the input image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to read the image.")
        return
    
    # Apply the averaging (smoothing) filter
    smoothed_image = cv2.blur(image, kernel_size)
    
    # Display the original and smoothed images
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.title(f"Averaging Filter (Kernel size {kernel_size})")
    plt.imshow(cv2.cvtColor(smoothed_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    plt.show()

# Example usage
apply_averaging_filter('C:\\Users\\DELL\\Pictures\\rani and srk.jpg', kernel_size=(2, 5))  # Replace with actual image path
