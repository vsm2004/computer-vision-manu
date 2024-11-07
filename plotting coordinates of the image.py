import cv2

def display_coordinates(image_path):
    """
    Displays an image and prints the coordinates of points clicked on the image.
    
    Parameters:
    - image_path: Path to the input image file.
    """
    # Read the image from the specified path
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image at path '{image_path}' could not be found.")
    
    # Callback function to handle mouse clicks
    def click_event(event, x, y, flags, param):
        # Check if the left mouse button was clicked
        if event == cv2.EVENT_LBUTTONDOWN:
            # Display the coordinates on the console
            print(f"Clicked coordinates: x={x}, y={y}")
            # Display the coordinates on the image
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image, f"{x}, {y}", (x, y), font, 0.5, (255, 0, 0), 1)
            cv2.imshow('Image', image)
    
    # Display the image in a window
    cv2.imshow('Image', image)
    # Set the mouse callback function to get coordinates
    cv2.setMouseCallback('Image', click_event)
    
    # Wait for a key to exit
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Example usage
image_path = 'C:\\Users\\DELL\\Pictures\\rani and srk.jpg'  # Replace with the path to your image file
display_coordinates(image_path)
