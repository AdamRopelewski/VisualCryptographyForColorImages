import cv2
from tiles import get_random_tile, colors


def is_pixel_is_bright(pixel):
    return pixel[2] > 127


def get_nears_basic_color(image_hsv, row, col):
    pixel = image_hsv[row, col]

    min_hue_distance = 1000.0
    min_saturation_distance = 1000.0
    min_brightness_distance = 1000.0
    closest_color = None

    for color in colors[1:-1]:
        hue_distance = 0.0
        saturation_distance = 0.0
        brightness_distance = 0.0
        hue_distance += abs(pixel[0] - color[0])
        saturation_distance += abs(pixel[1] - color[1])
        brightness_distance += abs(pixel[2] - color[2])
        if (
            hue_distance <= min_hue_distance
            and saturation_distance <= min_saturation_distance
            and brightness_distance <= min_brightness_distance
        ):
            closest_color = color
            min_hue_distance = hue_distance
            min_saturation_distance = saturation_distance
            min_brightness_distance = brightness_distance

    return list(closest_color)


def resize_image(image, x):
    """
    Resizes the given image to x times the resolution.
    """
    one_dim_size = x // 2
    new_image = cv2.resize(
        image, (image.shape[1] * one_dim_size, image.shape[0] * one_dim_size)
    )
    return new_image


def tile_invert(tile):
    return [[not i for i in tile[0]], [not i for i in tile[1]]]


def encode_images(image_hsv):
    # Create a new HSV image with 4x resolution
    encoded_hsv_image_1 = resize_image(image_hsv, 4)
    encoded_hsv_image_2 = resize_image(image_hsv, 4)
    encoded_hsv_image_3 = resize_image(image_hsv, 4)
    encoded_rgb_image_1 = cv2.cvtColor(encoded_hsv_image_1, cv2.COLOR_HSV2RGB)
    encoded_rgb_image_1_2 = cv2.cvtColor(encoded_hsv_image_1, cv2.COLOR_HSV2RGB)
    encoded_rgb_image_2 = cv2.cvtColor(encoded_hsv_image_2, cv2.COLOR_HSV2RGB)
    encoded_rgb_image_2_2 = cv2.cvtColor(encoded_hsv_image_2, cv2.COLOR_HSV2RGB)
    encoded_rgb_image_3 = cv2.cvtColor(encoded_hsv_image_3, cv2.COLOR_HSV2RGB)
    encoded_rgb_image_3_2 = cv2.cvtColor(encoded_hsv_image_3, cv2.COLOR_HSV2RGB)
    for row in range(image_hsv.shape[0]):
        for col in range(image_hsv.shape[1]):
            # nears_basic_color = get_nears_basic_color(image_hsv, row, col)
            tile = get_random_tile()
            for i in range(len(tile[0])):
                for j in range(len(tile[1])):
                    hue = image_hsv[row][col][0] % 256
                    saturation = image_hsv[row][col][1] % 256
                    brightness = image_hsv[row][col][2] % 256
                    if tile[i][j] == 1:
                        encoded_rgb_image_1[row * 2 + i][col * 2 + j] = [
                            brightness,
                            saturation,
                            hue,
                        ]
                        encoded_rgb_image_2[row * 2 + i][col * 2 + j] = [
                            saturation,
                            saturation,
                            saturation,
                        ]
                        encoded_rgb_image_3[row * 2 + i][col * 2 + j] = [
                            brightness,
                            brightness,
                            brightness,
                        ]
                    else:
                        encoded_rgb_image_1[row * 2 + i][col * 2 + j] = [0, 0, 0]
                        encoded_rgb_image_2[row * 2 + i][col * 2 + j] = [0, 0, 0]
                        encoded_rgb_image_3[row * 2 + i][col * 2 + j] = [0, 0, 0]
                    if not is_pixel_is_bright(image_hsv[row][col]):
                        tile = tile_invert(tile)
                    if tile[i][j] == 1:
                        encoded_rgb_image_1_2[row * 2 + i][col * 2 + j] = [
                            brightness,
                            saturation,
                            hue,
                        ]
                        encoded_rgb_image_2_2[row * 2 + i][col * 2 + j] = [
                            saturation,
                            saturation,
                            saturation,
                        ]
                        encoded_rgb_image_3_2[row * 2 + i][col * 2 + j] = [
                            brightness,
                            brightness,
                            brightness,
                        ]
                    else:
                        encoded_rgb_image_1_2[row * 2 + i][col * 2 + j] = [0, 0, 0]
                        encoded_rgb_image_2_2[row * 2 + i][col * 2 + j] = [0, 0, 0]
                        encoded_rgb_image_3_2[row * 2 + i][col * 2 + j] = [0, 0, 0]

    return (
        encoded_rgb_image_1,
        encoded_rgb_image_1_2,
        encoded_rgb_image_2,
        encoded_rgb_image_2_2,
        encoded_rgb_image_3,
        encoded_rgb_image_3_2,
    )


image = cv2.imread("input/ImageToBeCoded5.png")

# image = cv2.imread("input/test.png")
# Convert the image from RGB to HSV
image_hsv = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

(
    encoded_rgb_image_1,
    encoded_rgb_image_1_2,
    encoded_rgb_image_2,
    encoded_rgb_image_2_2,
    encoded_rgb_image_3,
    encoded_rgb_image_3_2,
) = encode_images(image_hsv)


# encoded_rgb_image_1 = cv2.cvtColor(encoded_hsv_image_1, cv2.COLOR_HSV2RGB)
# encoded_rgb_image_2 = cv2.cvtColor(encoded_hsv_image_2, cv2.COLOR_HSV2RGB)
# encoded_rgb_image_3 = cv2.cvtColor(encoded_hsv_image_3, cv2.COLOR_HSV2RGB)

# Display the image

cv2.imshow("Image", image)
cv2.imshow("Encoded1", encoded_rgb_image_1)
cv2.imshow("Encoded2", encoded_rgb_image_2)
cv2.imshow("Encoded3", encoded_rgb_image_3)
cv2.imshow("Encoded1_2", encoded_rgb_image_1_2)
cv2.imshow("Encoded2_2", encoded_rgb_image_2_2)
cv2.imshow("Encoded3_2", encoded_rgb_image_3_2)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("output/EncodedImage1.png", encoded_rgb_image_1)
cv2.imwrite("output/EncodedImage2.png", encoded_rgb_image_2)
cv2.imwrite("output/EncodedImage3.png", encoded_rgb_image_3)
cv2.imwrite("output/EncodedImage1_2.png", encoded_rgb_image_1_2)
cv2.imwrite("output/EncodedImage2_2.png", encoded_rgb_image_2_2)
cv2.imwrite("output/EncodedImage3_2.png", encoded_rgb_image_3_2)
