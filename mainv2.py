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
