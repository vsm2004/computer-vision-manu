from PIL import Image

# Open the image
image = Image.open('C:\\Users\\DELL\\Pictures\\rani and srk.jpg')  # Replace 'path_to_image.jpg' with your image file

# Convert the image to grayscale
gray_image = image.convert('L')

# Display the original and grayscale images
image.show(title="Original Image")
gray_image.show(title="Grayscale Image")
