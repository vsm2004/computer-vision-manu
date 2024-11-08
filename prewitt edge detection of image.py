import cv2
import numpy as np
import matplotlib.pyplot as plt

def prewitt_edge_detection(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Could not open or find the image.")
        return
    
    # Define the Prewitt kernels for horizontal and vertical edges
    prewitt_kernel_x = np.array([[1, 0, -1],
                                 [1, 0, -1],
                                 [1, 0, -1]])
    
    prewitt_kernel_y = np.array([[1, 1, 1],
                                 [0, 0, 0],
                                 [-1, -1, -1]])

    # Apply the Prewitt filter using convolution with the kernels
    edge_x = cv2.filter2D(image, -1, prewitt_kernel_x)  # Horizontal edges
    edge_y = cv2.filter2D(image, -1, prewitt_kernel_y)  # Vertical edges

    # Combine the edges to get the full edge map
    prewitt_edges = cv2.addWeighted(edge_x, 0.5, edge_y, 0.5, 0)
    
    # Plotting the images for comparison
    plt.figure(figsize=(10, 7))
    plt.subplot(1, 3, 1)
    plt.title("Original Image")
    plt.imshow(image, cmap='gray')
    
    plt.subplot(1, 3, 2)
    plt.title("Prewitt X Edge Detection")
    plt.imshow(edge_x, cmap='gray')
    
    plt.subplot(1, 3, 3)
    plt.title("Prewitt Y Edge Detection")
    plt.imshow(edge_y, cmap='gray')
    
    plt.figure()
    plt.title("Combined Prewitt Edge Detection")
    plt.imshow(prewitt_edges, cmap='gray')
    plt.show()

# Example usage
prewitt_edge_detection("C:\\Users\\DELL\\Pictures\\rani and srk.jpg")
