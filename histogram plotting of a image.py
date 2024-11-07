import cv2
import matplotlib.pyplot as plt

def plot_color_histogram(image_path):
    # Read the image in color
    image = cv2.imread(image_path)
    
    # Split the image into its color channels: B, G, R
    channels = cv2.split(image)
    colors = ('b', 'g', 'r')  # Blue, Green, Red
    plt.figure()
    plt.title('Color Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    
    # Loop through each channel and calculate the histogram
    for channel, color in zip(channels, colors):
        # Calculate histogram for each color channel
        hist = cv2.calcHist([channel], [0], None, [256], [0, 256])
        # Plot the histogram for the current color channel
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
    
    # Display the histogram
    plt.show()

# Example usage:
plot_color_histogram('C:\\Users\\DELL\\Pictures\\rani and srk.jpg')  # Replace 'path_to_image.jpg' with the actual path
