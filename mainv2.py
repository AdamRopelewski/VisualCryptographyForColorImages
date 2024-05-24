from PIL import Image
from tilesv2 import colors, colors_translated
import numpy as np


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


def random_tile(color=(255, 255, 255)):
    tile = Image.new("RGB", (2, 2))
    for i in range(2):
        for j in range(2):
            new_color = color
            if np.random.randint(0, 2) == 0:
                new_color = (0, 0, 0)

            tile.putpixel((i, j), new_color)
    return tile


image_path = "input/ImageToBeCoded5.png"
dithered_image = dither_image(image_path)
dithered_image.save("output/dithered_image.png")
dithered_image.show("dithered_image")

width = dithered_image.width
height = dithered_image.height

x3_res_dithered_image = Image.new("RGB", (width * 3, height * 3))

for x in range(width):
    for y in range(height):
        pixel_color = dithered_image.getpixel((x, y))
        for color_name, color_values in colors.items():
            if color_values == pixel_color:
                replacement_color = colors_translated[color_name]
                for i in range(3):
                    for j in range(3):
                        x3_res_dithered_image.putpixel(
                            (x * 3 + i, y * 3 + j), replacement_color[j][i]
                        )
                break
x3_res_dithered_image.save("output/x3_res_dithered_image.png")
x3_res_dithered_image.show()


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
encoded_image_1.save("output/encoded_image_1.png")
encoded_image_1.show()

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
encoded_image_2.save("output/encoded_image_2.png")
encoded_image_2.show()

decodedImage = Image.new("RGB", (width * 6, height * 6))
for x in range(width * 6):
    for y in range(height * 6):
        pixel_color1 = encoded_image_1.getpixel((x, y))
        pixel_color2 = encoded_image_2.getpixel((x, y))
        and_color = tuple(np.array(pixel_color1) & np.array(pixel_color2))
        decodedImage.putpixel((x, y), and_color)
decodedImage.save("output/decoded_image.png")
decodedImage.show()
