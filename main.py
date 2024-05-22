import cv2

image = cv2.imread("input/ImageToBeCoded.png")

# Convert the image from RGB to HSV
image_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)


# Display the image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
