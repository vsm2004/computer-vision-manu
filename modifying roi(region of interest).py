import cv2
import numpy as np
import matplotlib.pyplot as plt

def modify_roi(image_path, top_left, bottom_right, fill_color=(0, 255, 0)):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to read the image.")
        return
    
    # Define the Region of Interest (ROI)
    x1, y1 = top_left
    x2, y2 = bottom_right
    roi = image[y1:y2, x1:x2]
    
    # Fill the ROI with a solid color
    image[y1:y2, x1:x2] = fill_color
    
    # Display the original and modified images
    plt.figure(figsize=(10, 5))
    
    # Display the modified image with ROI filled
    plt.title("Modified Image with Filled ROI")
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    
    plt.show()

# Example usage
modify_roi('C:\\Users\\DELL\\Pictures\\rani and srk.jpg', top_left=(50, 50), bottom_right=(150, 150), fill_color=(0, 255, 0))  # Replace with actual image path
