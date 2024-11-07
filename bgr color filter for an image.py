import cv2
import numpy as np

def bgr_color_filter(image_path):
    """
    Load an image and apply a BGR color filter using trackbars.
    """
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print("Could not open or find the image.")
        return

    # Create a window
    cv2.namedWindow('BGR Color Filter')

    # Create trackbars for color change
    def update_filter(x):
        # Get current positions of the three trackbars
        blue = cv2.getTrackbarPos('Blue', 'BGR Color Filter')
        green = cv2.getTrackbarPos('Green', 'BGR Color Filter')
        red = cv2.getTrackbarPos('Red', 'BGR Color Filter')

        # Create a color filter based on trackbar values
        color_filter = np.zeros_like(img)
        color_filter[:] = [blue, green, red]

        # Apply the color filter
        filtered_img = cv2.addWeighted(img, 0.5, color_filter, 0.5, 0)
        
        # Display the filtered image
        cv2.imshow('BGR Color Filter', filtered_img)

    # Initial values for trackbars
    cv2.createTrackbar('Blue', 'BGR Color Filter', 0, 255, update_filter)
    cv2.createTrackbar('Green', 'BGR Color Filter', 0, 255, update_filter)
    cv2.createTrackbar('Red', 'BGR Color Filter', 0, 255, update_filter)

    # Display the initial image
    update_filter(0)

    # Keep the window open until 'Esc' is pressed
    while True:
        if cv2.waitKey(1) & 0xFF == 27:  # 'Esc' key to exit
            break

    cv2.destroyAllWindows()

# Run the function with your image path
bgr_color_filter('C:\\Users\\DELL\\Pictures\\rani and srk.jpg')
