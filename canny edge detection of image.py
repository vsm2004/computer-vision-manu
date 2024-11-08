import cv2
import matplotlib.pyplot as plt

def canny_edge_detection(image_path, lower_threshold=50, upper_threshold=150):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        print("Could not open or find the image.")
        return
    
    # Step 1: Apply Gaussian Blur to reduce noise
    blurred_image = cv2.GaussianBlur(image, (5, 5), 1.4)
    
    # Step 2: Apply Canny Edge Detector
    canny_edges = cv2.Canny(blurred_image, lower_threshold, upper_threshold)
    
    # Display the original and the Canny edge-detected images
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(image, cmap='gray')
    
    plt.subplot(1, 2, 2)
    plt.title("Canny Edge Detection")
    plt.imshow(canny_edges, cmap='gray')
    plt.show()

# Example usage
canny_edge_detection("C:\\Users\\DELL\\Pictures\\rani and srk.jpg", lower_threshold=50, upper_threshold=150)
