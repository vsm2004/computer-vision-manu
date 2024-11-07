import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_erosion(image_path, kernel_size=(5, 5), iterations=1):
    # Load the input image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Error: Unable to read the image.")
        return

    # Define the erosion kernel (structuring element)
    kernel = np.ones(kernel_size, np.uint8)

    # Apply the erosion operation
    eroded_image = cv2.erode(image, kernel, iterations=iterations)

    # Display the original and eroded images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("Eroded Image")
    plt.imshow(eroded_image, cmap='gray')
    plt.axis('off')

    plt.show()

# Example usage
apply_erosion('C:\\Users\\DELL\\Pictures\\rani and srk.jpg', kernel_size=(5, 5), iterations=1)  # Replace with actual image path
