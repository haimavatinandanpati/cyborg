import cv2

# Loading of the image
image = cv2.imread(r"C:\Users\Haimavatinandan\Downloads\IP_BASICS.jpg")

# assigning the variables the data to be printed
name = 'HAIMAVATINANDAN PATI'
roll_number = '122EE0607'
version = cv2.__version__
text = f'{name} | {roll_number} | OpenCV {version}'

# Setting of the font and size of text
font = cv2.FONT_HERSHEY_TRIPLEX
font_scale = .6
font_thickness = 1

# Get the size of the text
text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)

# Calculating the position of the text in the bottom right corner
text_position = (730, 750)

# Adding the text to the image
cv2.putText(image, text, text_position, font, font_scale, (60, 0, 250), font_thickness, cv2.LINE_AA)

# Displaying the image
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(image.shape)

