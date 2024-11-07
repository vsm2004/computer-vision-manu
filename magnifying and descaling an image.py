import cv2

# Step 1: Read the original image
image = cv2.imread('C:\\Users\\DELL\\Pictures\\rani and srk.jpg')  # Replace 'path_to_image.jpg' with your actual image path

# Step 2: Resize the image to smaller dimensions
# Set new width and height (e.g., half of the original size)
smaller_image = cv2.resize(image, (0, 0), fx=0.5, fy=0.5)

# Step 3: Resize the image to larger dimensions
# Set new width and height (e.g., double the original size)
larger_image = cv2.resize(image, (0, 0), fx=2.0, fy=2.0)

# Step 4: Display the original, smaller, and larger images
cv2.imshow('Original Image', image)
cv2.imshow('Smaller Image', smaller_image)
cv2.imshow('Larger Image', larger_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
