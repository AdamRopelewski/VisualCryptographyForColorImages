import numpy as np


def get_tile(tile_id):
    return tiles[tile_id - 1]


def get_random_tile():
    return tiles[np.random.randint(0, 16)]


# Define the tiles
tiles = [
    np.array([[1, 1], [1, 1]]),  # Tile 1
    np.array([[1, 1], [1, 0]]),  # Tile 2
    np.array([[1, 1], [0, 1]]),  # Tile 3
    np.array([[1, 1], [0, 0]]),  # Tile 4
    np.array([[1, 0], [1, 1]]),  # Tile 5
    np.array([[1, 0], [1, 0]]),  # Tile 6
    np.array([[1, 0], [0, 1]]),  # Tile 7
    np.array([[1, 0], [0, 0]]),  # Tile 8
    np.array([[0, 1], [1, 1]]),  # Tile 9
    np.array([[0, 1], [1, 0]]),  # Tile 10
    np.array([[0, 1], [0, 1]]),  # Tile 11
    np.array([[0, 1], [0, 0]]),  # Tile 12
    np.array([[0, 0], [1, 1]]),  # Tile 13
    np.array([[0, 0], [1, 0]]),  # Tile 14
    np.array([[0, 0], [0, 1]]),  # Tile 15
    np.array([[0, 0], [0, 0]]),  # Tile 16
]
