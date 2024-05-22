import numpy as np


# def get_random_tile():
#     n = len(colorfull_tiles)
#     return colorfull_tiles[np.random.randint(0, n)]


def get_random_tile():
    return tiles[np.random.randint(0, 16)]


# Define the tiles
tiles = [
    [[1, 1], [1, 1]],  # Tile 1
    [[1, 1], [1, 0]],  # Tile 2
    [[1, 1], [0, 1]],  # Tile 3
    [[1, 1], [0, 0]],  # Tile 4
    [[1, 0], [1, 1]],  # Tile 5
    [[1, 0], [1, 0]],  # Tile 6
    [[1, 0], [0, 1]],  # Tile 7
    [[1, 0], [0, 0]],  # Tile 8
    [[0, 1], [1, 1]],  # Tile 9
    [[0, 1], [1, 0]],  # Tile 10
    [[0, 1], [0, 1]],  # Tile 11
    [[0, 1], [0, 0]],  # Tile 12
    [[0, 0], [1, 1]],  # Tile 13
    [[0, 0], [1, 0]],  # Tile 14
    [[0, 0], [0, 1]],  # Tile 15
    [[0, 0], [0, 0]],  # Tile 16
]

# Define the tiles cv2 in hsv format
black = (0, 0, 0)
blue = (0, 255, 255)
red = (120, 255, 255)
green = (60, 255, 255)
white = (0, 0, 255)
colors = [black, red, green, blue, white]

# n = len(colors)
# colorfull_tiles = []
# for i in range(n):
#     for k in range(n):
#         for j in range(n):
#             for l in range(n):
#                 colorfull_tiles.append([[colors[i], colors[k]], [colors[j], colors[l]]])
# print(colorfull_tiles)
