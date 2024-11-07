import cv2
import numpy as np
import matplotlib.pyplot as plt

def rotate_image_y_axis(image_path):
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to read the image.")
        return

    # Flip the image along the y-axis (creating a mirror image effect)
    flipped_image = cv2.flip(image, 1)

    # Rotate the flipped image 90 degrees clockwise
    rotated_image = cv2.rotate(flipped_image, cv2.ROTATE_90_CLOCKWISE)

    # Display the original and rotated images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("Rotated Image (90° along Y-axis)")
    plt.imshow(cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

    plt.show()

# Example usage:
rotate_image_y_axis('C:\\Users\\DELL\\Pictures\\rani and srk.jpg')  # Replace with your actual image path
