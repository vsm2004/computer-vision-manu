import cv2

def find_contour_coordinates(image_path):
    """
    Finds and displays the coordinates of contours in an image.
    """
    # Load the image
    img = cv2.imread(image_path)
    if img is None:
        print("Could not open or find the image.")
        return

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to get a binary image
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original image for visualization
    cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

    # Print contour points
    for i, contour in enumerate(contours):
        print(f"Contour {i + 1}:")
        for point in contour:
            x, y = point[0]  # Extract x and y coordinates
            print(f"({x}, {y})")
            # You can also mark each point on the image for visualization
            cv2.circle(img, (x, y), 3, (255, 0, 0), -1)

    # Display the image with contours
    cv2.imshow("Contours", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Run the function with your image path
find_contour_coordinates("C:\\Users\\DELL\\Pictures\\rani and srk.jpg")
