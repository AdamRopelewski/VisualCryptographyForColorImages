from PIL import Image
from tilesv2 import colors, colors_translated
import numpy as np


def random_tile(color=(255, 255, 255)):
    tile = Image.new("RGB", (2, 2))
    for i in range(2):
        for j in range(2):
            new_color = color
            if np.random.randint(0, 2) == 0:
                new_color = (0, 0, 0)

            tile.putpixel((i, j), new_color)
    return tile


def dither_image(image_path):
    palette = []
    for color in colors.values():
        palette.extend(color)

    image = Image.open(image_path)
    if image.mode != "RGB":
        image = image.convert("RGB")

    palette_image = Image.new("P", (1, 1))
    palette_image.putpalette(palette)

    dithered_image = image.quantize(palette=palette_image, dither=Image.FLOYDSTEINBERG)

    safe_image = dithered_image.convert("RGB")

    return safe_image


def create_x3_res_dithered_made_of_tiles_image(
    dithered_image, colors, colors_translated
):
    width = dithered_image.width
    height = dithered_image.height

    x3_res_dithered_made_of_tiles_image = Image.new("RGB", (width * 3, height * 3))

    for x in range(width):
        for y in range(height):
            pixel_color = dithered_image.getpixel((x, y))
            for color_name, color_values in colors.items():
                if color_values == pixel_color:
                    replacement_color = colors_translated[color_name]
                    for i in range(3):
                        for j in range(3):
                            x3_res_dithered_made_of_tiles_image.putpixel(
                                (x * 3 + i, y * 3 + j), replacement_color[j][i]
                            )
                    break

    return x3_res_dithered_made_of_tiles_image


def encode_image(width, height):
    encoded_image_1 = Image.new("RGB", (width * 6, height * 6))

    for x in range(width):
        for y in range(height):
            for i in range(3):
                for j in range(3):
                    encoded_image_1.paste(
                        random_tile(
                            (
                                255 if i == 0 else 0,
                                255 if i == 1 else 0,
                                255 if i == 2 else 0,
                            )
                        ),
                        (x * 6 + i * 2, y * 6 + j * 2),
                    )

    return encoded_image_1


def decode_images(encoded_image_1, encoded_image_2):
    width = encoded_image_1.width
    height = encoded_image_1.height

    decoded_image = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            pixel_color1 = encoded_image_1.getpixel((x, y))
            pixel_color2 = encoded_image_2.getpixel((x, y))
            and_color = tuple(np.array(pixel_color1) & np.array(pixel_color2))
            decoded_image.putpixel((x, y), and_color)

    return decoded_image


image_path = "input/ImageToBeCoded5.png"

dithered_image = dither_image(image_path)

dithered_image.save("output/1_dithered_image.png")
dithered_image.show("dithered_image")
print("1/5: dithered_image")

width = dithered_image.width
height = dithered_image.height


x3_res_dithered_image = create_x3_res_dithered_made_of_tiles_image(
    dithered_image, colors, colors_translated
)
x3_res_dithered_image.save("output/2_x3_res_dithered_image.png")
x3_res_dithered_image.show()
print("2/5: x3_res_dithered_image")


encoded_image_1 = encode_image(width, height)
encoded_image_1.save("output/3_encoded_image_1.png")
encoded_image_1.show()
print("3/5: encoded_image_1")


encoded_image_2 = Image.new("RGB", (width * 6, height * 6))

for x in range(width * 3):
    for y in range(height * 3):
        pixel_color = x3_res_dithered_image.getpixel((x, y))
        if pixel_color == (0, 0, 0):
            tile = Image.new("RGB", (2, 2))
            for i in range(2):
                for j in range(2):
                    tile.putpixel(
                        (i, j),
                        tuple(
                            np.array(encoded_image_1.getpixel((x * 2 + i, y * 2 + j)))
                            ^ np.array(
                                (
                                    255 if x % 3 == 0 else 0,
                                    255 if x % 3 == 1 else 0,
                                    255 if x % 3 == 2 else 0,
                                )
                            )
                        ),
                    )
            encoded_image_2.paste(tile, (x * 2, y * 2))
        else:
            encoded_image_2.paste(
                random_tile(
                    (
                        255 if x % 3 == 0 else 0,
                        255 if x % 3 == 1 else 0,
                        255 if x % 3 == 2 else 0,
                    )
                ),
                (x * 2, y * 2),
            )
encoded_image_2.save("output/4_encoded_image_2.png")
encoded_image_2.show()
print("4/5: encoded_image_2")


decoded_image = decode_images(encoded_image_1, encoded_image_2)
decoded_image.save("output/5_decoded_image.png")
decoded_image.show()
print("5/5: decoded_image")
