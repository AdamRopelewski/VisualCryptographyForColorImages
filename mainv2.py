from PIL import Image

# Definicje kolorów
colors = {
    'dark gray': (64, 64, 64),
    'black': (0, 0, 0),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'light gray': (192, 192, 192),
    'white': (255, 255, 255),
    'cyan': (0, 255, 255),
    'magenta': (255, 0, 255),
    'yellow': (255, 255, 0)
}

colors_translated = {
    'dark gray': [
        [ (0, 0, 0), (0, 0, 0), (0, 0, 0) ],
        [ (255, 0, 0), (0, 255, 0), (0, 0, 255) ],
        [ (0, 0, 0), (0, 0, 0), (0, 0, 0) ]
    ],
    'black': [
        [ (0, 0, 0), (0, 0, 0), (0, 0, 0) ],
        [ (0, 0, 0), (0, 0, 0), (0, 0, 0) ],
        [ (0, 0, 0), (0, 0, 0), (0, 0, 0) ]
    ],
    'red': [
        [ (255, 0, 0), (0, 0, 0), (0, 0, 0) ],
        [ (255, 0, 0), (0, 0, 0), (0, 0, 0) ],
        [ (255, 0, 0), (0, 0, 0), (0, 0, 0) ]
    ],
    'green': [
        [ (0, 0, 0), (0, 255, 0), (0, 0, 0) ],
        [ (0, 0, 0), (0, 255, 0), (0, 0, 0) ],
        [ (0, 0, 0), (0, 255, 0), (0, 0, 0) ]
    ],
    'blue': [
        [ (0, 0, 0), (0, 0, 0), (0, 0, 255) ],
        [ (0, 0, 0), (0, 0, 0), (0, 0, 255) ],
        [ (0, 0, 0), (0, 0, 0), (0, 0, 255) ]
    ],
    'light gray': [
        [ (255, 0, 0), (0, 255, 0), (0, 0, 255) ],
        [ (0, 0, 0), (0, 0, 0), (0, 0, 0)  ],
        [ (255, 0, 0), (0, 255, 0), (0, 0, 255) ]
    ],
    'white': [
        [ (255, 0, 0), (0, 255, 0), (0, 0, 255) ],
        [ (255, 0, 0), (0, 255, 0), (0, 0, 255) ],
        [ (255, 0, 0), (0, 255, 0), (0, 0, 255) ]
    ],
    'cyan': [
        [ (0, 0, 0), (0, 255, 0), (0, 0, 255) ],
        [ (0, 0, 0), (0, 255, 0), (0, 0, 255) ],
        [ (0, 0, 0), (0, 255, 0), (0, 0, 255) ]
    ],
    'magenta': [
        [ (255, 0, 0), (0, 0, 0), (0, 0, 255) ],
        [ (255, 0, 0), (0, 0, 0), (0, 0, 255) ],
        [ (255, 0, 0), (0, 0, 0), (0, 0, 255) ]
    ],
    'yellow': [
        [ (255, 0, 0), (0, 255, 0), (0, 0, 0) ],
        [ (255, 0, 0), (0, 255, 0), (0, 0, 0) ],
        [ (255, 0, 0), (0, 255, 0), (0, 0, 0) ]
    ]
}

n1 = 5
n2 = 2

# Tworzenie obrazu o wymiarach 5x2
img = Image.new('RGB', (n1, n2))

# Wypełnianie obrazu kolorami
for x, color in enumerate(colors.values()):
    img.putpixel((x%n1, x//n1), color)

img2 = Image.new('RGB', (n1*3, n2*3))

for x in range(n1):
    for y in range(n2):
        pixel_color = img.getpixel((x, y))
        for color_name, color_values in colors.items():
            if color_values == pixel_color:
                replacement_color = colors_translated[color_name]
                for i in range(3):
                    for j in range(3):
                        img2.putpixel((x*3 + i, y*3 + j), replacement_color[j][i])
                break


# Wyświetlanie obrazu
img.show()
img2.show()

import numpy as np

def random_tile(color=(255, 255, 255)):
    tile = Image.new('RGB', (2, 2))
    for i in range(2):
        for j in range(2):
            new_color = color
            if np.random.randint(0, 2) == 0:
                new_color = (0, 0, 0)

            tile.putpixel((i, j), new_color)
    return tile

img3 = Image.new('RGB', (n1*6, n2*6))

for x in range(n1):
    for y in range(n2):
        for i in range(3):
            for j in range(3):
                img3.paste(random_tile((255 if i==0 else 0, 255 if i==1 else 0, 255 if i==2 else 0)), (x*6 + i*2, y*6 + j*2))

img3.show()

img4 = Image.new('RGB', (n1*6, n2*6))

for x in range(n1*3):
    for y in range(n2*3):
        pixel_color = img2.getpixel((x, y))
        if pixel_color == (0, 0, 0):
            tile = Image.new('RGB', (2, 2))
            for i in range(2):
                for j in range(2):
                    tile.putpixel((i, j), tuple(np.array(img3.getpixel((x*2 + i, y*2 + j))) ^ np.array((255 if x%3==0 else 0, 255 if x%3==1 else 0, 255 if x%3==2 else 0))))
            img4.paste(tile, (x*2, y*2))
        else:
            img4.paste(random_tile((255 if x%3==0 else 0, 255 if x%3==1 else 0, 255 if x%3==2 else 0)), (x*2, y*2))

img4.show()

img5 = Image.new('RGB', (n1*6, n2*6))
for x in range(n1*6):
    for y in range(n2*6):
        pixel_color1 = img3.getpixel((x, y))
        pixel_color2 = img4.getpixel((x, y))
        and_color = tuple(np.array(pixel_color1) & np.array(pixel_color2))
        img5.putpixel((x, y), and_color)
img5.show()
