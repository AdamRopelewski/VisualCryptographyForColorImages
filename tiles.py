import numpy as np


def get_random_tile():
    n = len(colorfull_tiles)
    return colorfull_tiles[np.random.randint(0, n)]


# Define the tiles cv2 in hsv format
black = (0, 0, 0)
blue = (0, 255, 255)
red = (120, 255, 255)
green = (60, 255, 255)
white = (0, 0, 255)
colors = [black, blue, red, green, white]

n = len(colors)
colorfull_tiles = []
for i in range(n):
    for k in range(n):
        for j in range(n):
            for l in range(n):
                colorfull_tiles.append([[colors[i], colors[k]], [colors[j], colors[l]]])
print(colorfull_tiles)
