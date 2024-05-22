import cv2
from tiles import get_tile, get_random_tile


def modify_pixels_brightness(image_hsv, row, col, new_brightness):
    """
    Modifies the pixels saturation value at the specified row and column in the given HSV image.
    """
    pixel = image_hsv[row, col]
    pixel[2] = new_brightness
    image_hsv[row, col] = pixel
    return image_hsv


image = cv2.imread("input/ImageToBeCoded.png")

# Convert the image from RGB to HSV
image_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)


def check_if_bright_pixel(image_hsv, row, col):
    """
    Checks if the pixel at the specified row and column in the given HSV image has a brightness value greater than 0.5.
    """
    pixel = image_hsv[row, col]
    if pixel[2] > 0.5:
        return True


def encode_images(image_hsv):
    # Create a new HSV image with 4x resolution
    encoded_hsv_image_1 = cv2.resize(
        image_hsv, (image_hsv.shape[1] * 2, image_hsv.shape[0] * 2)
    )
    encoded_hsv_image_2 = cv2.resize(
        image_hsv, (image_hsv.shape[1] * 2, image_hsv.shape[0] * 2)
    )

    for row in range(image_hsv.shape[0]):
        for col in range(image_hsv.shape[1]):
            tile = get_random_tile()
            for i in range(2):
                for j in range(2):
                    # Check if the pixel is bright
                    if tile[i, j] == 1:
                        saturation = 1
                    else:
                        saturation = 0
                    # Update the pixel's saturation value
                    encoded_hsv_image_1 = modify_pixels_brightness(
                        encoded_hsv_image_1, row * 2 + i, col * 2 + j, saturation
                    )
                    if not check_if_bright_pixel(image_hsv, row, col):
                        saturation *= -1
                    encoded_hsv_image_2 = modify_pixels_brightness(
                        encoded_hsv_image_2, row * 2 + i, col * 2 + j, saturation
                    )

    return encoded_hsv_image_1, encoded_hsv_image_2


encoded_hsv_image_1, encoded_hsv_image_2 = encode_images(image_hsv)
# Display the image
cv2.imshow("Image", image)
cv2.imshow("Encoded1", encoded_hsv_image_1)
cv2.imshow("Encoded2", encoded_hsv_image_2)
cv2.waitKey(0)
cv2.destroyAllWindows()


# # Convert the image back to RGB
# image_modified = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)
