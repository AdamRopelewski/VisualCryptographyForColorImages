import cv2
from tiles import get_tile


def modify_pixel(image_hsv, row, col, new_value):
    """
    Modifies the pixels saturation value at the specified row and column in the given HSV image.
    """
    pixel = image_hsv[row, col]
    pixel[1] = new_value
    image_hsv[row, col] = pixel
    return image_hsv


image = cv2.imread("input/ImageToBeCoded.png")

# Convert the image from RGB to HSV
image_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)


# Display the image
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Convert the image back to RGB
image_modified = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)

# Display the modified image
cv2.imshow("Modified Image", image_modified)
cv2.waitKey(0)
cv2.destroyAllWindows()
