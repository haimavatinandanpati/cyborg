import cv2

# Load the image
image = cv2.imread(r"C:\Users\Haimavatinandan\Downloads\IP_BASICS.jpg")

# Define the text to display
name = 'HAIMAVATINANDAN PATI'
roll_number = '122EE0607'
version = cv2.__version__
text = f'{name} | {roll_number} | OpenCV {version}'

# Set the font properties
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
font_thickness = 2

# Get the size of the text
text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)

# Calculate the position of the text in the bottom right corner
text_position = (image.shape[1] - text_size[0] - 10, image.shape[0] - 10)

# Add the text to the image
cv2.putText(image, text, text_position, font, font_scale, (0, 0, 255), font_thickness, cv2.LINE_AA)

# Display the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
