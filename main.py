from PIL import Image
from colors import colors, colors_translated
import numpy as np
import concurrent.futures
import time
import os


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


def create_x9_res_dithered_made_of_tiles_image(
    dithered_image, colors, colors_translated, max_threads=4
):
    """
    Creates an image thats made of RGB (255) and Black.
    Those mix into the original colors.
    Each pixel now is represented by a 3.

    """
    width = dithered_image.width
    height = dithered_image.height

    x9_res_dithered_made_of_tiles_image = Image.new("RGB", (width * 3, height * 3))

    def process_pixel(x):
        for y in range(height):
            pixel_color = dithered_image.getpixel((x, y))
            for color_name, color_values in colors.items():
                if color_values == pixel_color:
                    replacement_color = colors_translated[color_name]
                    for i in range(3):
                        for j in range(3):
                            x9_res_dithered_made_of_tiles_image.putpixel(
                                (x * 3 + i, y * 3 + j), replacement_color[j][i]
                            )
                    break

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        for x in range(width):
            executor.submit(process_pixel, x)

    return x9_res_dithered_made_of_tiles_image


def encode_image(original_width, original_height, max_threads=4):
    """
    Creates an image encrypted that is made of 2x2 random tiles.
    Those are made of R or G or B (255) and Black.
    """
    total_pixels = original_width * 6, original_height * 6
    encoded_image_1 = Image.new("RGB", (original_width * 6, original_height * 6))

    def generate_tile(x):
        # Generate a random tile with the corresponding color (R or G or B)
        for y in range(original_height):
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
                        # Paste the tile in the corresponding position
                        (x * 6 + i * 2, y * 6 + j * 2),
                    )

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        for x in range(original_width):
            executor.submit(generate_tile, x)

    return encoded_image_1


def encode_image_2(
    original_width,
    original_height,
    x3_res_dithered_made_of_tiles_image,
    encoded_image_1,
    max_threads=4,
):
    """
    Encodes the second image.
    """
    encoded_image_2 = Image.new("RGB", (original_width * 6, original_height * 6))

    def generate_tile(x):
        for y in range(original_height * 3):
            pixel_color = x3_res_dithered_made_of_tiles_image.getpixel((x, y))
            # If the pixel is black, we paste the corresponding tile based on the first image
            if pixel_color == (0, 0, 0):
                tile = Image.new("RGB", (2, 2))
                for i in range(2):
                    for j in range(2):
                        encoded_pixel_from_im_1 = encoded_image_1.getpixel(
                            (x * 2 + i, y * 2 + j)
                        )
                        tile_pixel = (
                            255 if x % 3 == 0 else 0,
                            255 if x % 3 == 1 else 0,
                            255 if x % 3 == 2 else 0,
                        )
                        # XOR the encoded pixel from first encode image with the tile pixel
                        new_pixel = tuple(
                            np.array(encoded_pixel_from_im_1) ^ np.array(tile_pixel)
                        )
                        tile.putpixel((i, j), new_pixel)
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

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        for x in range(original_width * 3):
            executor.submit(generate_tile, x)

    return encoded_image_2


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


def restore_colors_and_res(decoded_image):
    decoded_width = decoded_image.width
    decoded_height = decoded_image.height
    original_height = decoded_height // 6
    original_width = decoded_width // 6

    decoded_image_restored_colors = Image.new("RGB", (original_width, original_height))
    for x in range(original_width):
        for y in range(original_height):
            sum_r = 0
            sum_g = 0
            sum_b = 0
            sum_black = 0
            for i in range(6):
                for j in range(6):
                    decoded_pixel_from_im_1 = decoded_image.getpixel(
                        (x * 6 + i, y * 6 + j)
                    )
                    if decoded_pixel_from_im_1 == (255, 0, 0):
                        sum_r += 1
                    elif decoded_pixel_from_im_1 == (0, 255, 0):
                        sum_g += 1
                    elif decoded_pixel_from_im_1 == (0, 0, 255):
                        sum_b += 1
                    else:
                        sum_black += 1
            restored_color = (255 * sum_r // 9, 255 * sum_g // 9, 255 * sum_b // 9)
            if sum_r == 0 and sum_g == 0 and sum_b == 0:
                restored_color = (0, 0, 0)
            decoded_image_restored_colors.putpixel((x, y), restored_color)
    return decoded_image_restored_colors


def encode(image_path, max_threads=4, progress_var=None, cwd=""):
    dithered_image = dither_image(image_path)
    if progress_var:
        progress_var.set(0)
    dithered_image.save(cwd + "output/1_dithered_image.png")
    if progress_var:
        progress_var.set(5.0)  # 1/4 stages completed
    print("1/6: dithered_image")
    original_width = dithered_image.width
    original_height = dithered_image.height

    x3_res_dithered_made_of_tiles_image = create_x9_res_dithered_made_of_tiles_image(
        dithered_image, colors, colors_translated, max_threads=max_threads
    )
    x3_res_dithered_made_of_tiles_image.save(
        cwd + "output/2_x9_res_dithered_made_of_tiles_image.png"
    )
    if progress_var:
        progress_var.set(20.0)  # 2/4 stages completed
    print("2/6: x9_res_dithered_image")
    encoded_image_1 = encode_image(
        original_width, original_height, max_threads=max_threads
    )
    encoded_image_1.save(cwd + "output/3_encoded_image_1.png")
    if progress_var:
        progress_var.set(60.0)  # 3/4 stages completed
    print("3/6: encoded_image_1")
    encoded_image_2 = encode_image_2(
        original_width,
        original_height,
        x3_res_dithered_made_of_tiles_image,
        encoded_image_1,
        max_threads=max_threads,
    )
    encoded_image_2.save(cwd + "output/4_encoded_image_2.png")
    if progress_var:
        progress_var.set(100.0)  # 4/4 stages completed
    print("4/6: encoded_image_2 ~ 80%")


def decode(file_path_1, file_path_2, max_threads=4, progress_var=None, cwd=""):
    encoded_image_1 = Image.open(file_path_1)
    encoded_image_2 = Image.open(file_path_2)

    decoded_image = decode_images(encoded_image_1, encoded_image_2)
    decoded_image.save(cwd + "output/5_decoded_image_xor_and.png")
    if progress_var:
        progress_var.set(80.0)  # 1/2 stages completed
    print("5/6: decoded_image")
    decoded_image_restored_colors = restore_colors_and_res(decoded_image)
    decoded_image_restored_colors.save(
        cwd + "output/6_decoded_image_restored_colors.png"
    )

    if progress_var:
        progress_var.set(100.0)  # 2/2 stages completed
    print("6/6: decoded_image_restored_colors")


if __name__ == "__main__":
    max_threads = 8
    time_start = time.time()
    image_path = "input/ImageToBeCoded0.png"
    encode(image_path, max_threads=max_threads)
    decode(
        "output/3_encoded_image_1.png",
        "output/4_encoded_image_2.png",
        max_threads=max_threads,
    )
    print("Time taken: ", time.time() - time_start)
