import tkinter as tk
from tkinter import filedialog
import main


def encode():
    file_path = filedialog.askopenfilename()
    main.encode(file_path, max_threads=8)


def decode():
    # output_dir = filedialog.askdirectory()
    main.decode(
        "output/3_encoded_image_1.png", "output/4_encoded_image_2.png", max_threads=8
    )


# Create the main window
window = tk.Tk()
window.title("Visual Cryptography")
window.geometry("400x200")


# Encoding and decoding buttons
encode_button = tk.Button(window, text="Encode", command=encode)
encode_button.pack(pady=10)

decode_button = tk.Button(window, text="Decode", command=decode)
decode_button.pack(pady=10)

# Start the main loop
window.mainloop()
