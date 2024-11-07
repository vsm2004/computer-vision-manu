import cv2
import numpy as np

def translate_image(image_path, x_shift, y_shift):
    """
    Reads an image from the specified path and translates it by x_shift and y_shift.
    
    Parameters:
    - image_path: Path to the input image file.
    - x_shift: The number of pixels to shift the image along the x-axis.
    - y_shift: The number of pixels to shift the image along the y-axis.
    
    Returns:
    - Translated image.
    """
    # Read the image from the given path
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image at path '{image_path}' could not be found.")

    # Get image dimensions
    height, width = image.shape[:2]
    
    # Define the translation matrix
    translation_matrix = np.float32([[1, 0, x_shift], [0, 1, y_shift]])
    
    # Apply the translation
    translated_image = cv2.warpAffine(image, translation_matrix, (width, height))
    
    return translated_image

# Example usage
image_path = 'C:\\Users\\DELL\\Pictures\\rani and srk.jpg'  # Replace with your image file path
x_shift = 100  # Translate 100 pixels to the right
y_shift = 50   # Translate 50 pixels down

translated_image = translate_image(image_path, x_shift, y_shift)

# Display the result
cv2.imshow('Original Image', cv2.imread(image_path))
cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


