from PIL import Image as img
import numpy as np

image = img.open("input/image_to_be_coded.png")
image = image.convert('RGB')
pixels = np.array(image)

height, width, _ = pixels.shape

share1 = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
share2 = np.zeros_like(share1)

for i in range(height):
    for j in range(width):
        for k in range(3):
            share2[i, j, k] = pixels[i, j, k] ^ share1[i, j, k]

share1_image = img.fromarray(share1)
share2_image = img.fromarray(share2)
decoded_image = img.fromarray(share1 ^ share2)

share1_image.show()
share2_image.show()
decoded_image.show()
