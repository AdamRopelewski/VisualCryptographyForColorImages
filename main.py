import cv2
from tiles import get_tile, get_random_tile


def modify_pixels_brightness(image, row, col, new_brightness):
    """
    Modifies the pixels brightness value at the specified row and column in the given HSV image.
    """
    pixel = image[row, col]
    pixel[2] = new_brightness
    image[row, col] = pixel
    return image


def modify_pixels_saturation(image, row, col, new_saturation):
    """
    Modifies the pixels saturation value at the specified row and column in the given HSV image.
    """
    pixel = image[row, col]
    pixel[1] = new_saturation
    image[row, col] = pixel
    return image


def modify_pixels_hue(image, row, col, new_hue):
    """
    Modifies the pixels hue value at the specified row and column in the given HSV image.
    """
    pixel = image[row, col]
    pixel[0] = new_hue % 179
    image[row, col] = pixel
    return image


def check_if_bright_pixel(image_hsv, row, col):
    """
    Checks if the pixel at the specified row and column in the given HSV image has a brightness value greater than 0.5.
    """
    pixel = image_hsv[row, col]
    if pixel[2] > 127:
        return True
    return False


def resize_image(image, x):
    """
    Resizes the given image to x times the resolution.
    """
    one_dim_size = x // 2
    new_image = cv2.resize(
        image, (image.shape[1] * one_dim_size, image.shape[0] * one_dim_size)
    )
    return new_image


def encode_images(image_hsv):
    # Create a new HSV image with 4x resolution
    encoded_hsv_image_1 = resize_image(image_hsv, 4)
    encoded_hsv_image_2 = resize_image(image_hsv, 4)
    for row in range(image_hsv.shape[0]):
        for col in range(image_hsv.shape[1]):
            tile = get_random_tile()
            for i in range(len(tile[0])):
                for j in range(len(tile[1])):
                    # Check if the pixel is bright
                    if tile[i][j] == 1:
                        brightness = 0
                    else:
                        brightness = 255 // 2
                    encoded_hsv_image_1 = modify_pixels_brightness(
                        encoded_hsv_image_1, row * 2 + i, col * 2 + j, brightness
                    )
                    encoded_hsv_image_1 = modify_pixels_saturation(
                        encoded_hsv_image_1, row * 2 + i, col * 2 + j, brightness
                    )
                    encoded_hsv_image_1 = modify_pixels_hue(
                        encoded_hsv_image_1, row * 2 + i, col * 2 + j, brightness
                    )

                    if not check_if_bright_pixel(image_hsv, row, col):
                        brightness = 255 // 2 - brightness

                    encoded_hsv_image_2 = modify_pixels_brightness(
                        encoded_hsv_image_2, row * 2 + i, col * 2 + j, brightness
                    )
                    encoded_hsv_image_2 = modify_pixels_saturation(
                        encoded_hsv_image_2, row * 2 + i, col * 2 + j, brightness
                    )
                    encoded_hsv_image_2 = modify_pixels_hue(
                        encoded_hsv_image_2, row * 2 + i, col * 2 + j, brightness
                    )

    return encoded_hsv_image_1, encoded_hsv_image_2


image = cv2.imread("input/ImageToBeCoded.png")


# Convert the image from RGB to HSV
image_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)


encoded_hsv_image_1, encoded_hsv_image_2 = encode_images(image_hsv)
encoded_rgb_image_1 = cv2.cvtColor(encoded_hsv_image_1, cv2.COLOR_HSV2RGB)
encoded_rgb_image_2 = cv2.cvtColor(encoded_hsv_image_2, cv2.COLOR_HSV2RGB)
# Display the image
cv2.imwrite("output/EncodedImage1.png", encoded_rgb_image_1)
cv2.imwrite("output/EncodedImage2.png", encoded_rgb_image_2)
cv2.imshow("Image", image)
cv2.imshow("Encoded1", encoded_rgb_image_1)
cv2.imshow("Encoded2", encoded_rgb_image_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
