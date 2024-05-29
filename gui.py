import os
import tkinter as tk
import threading
import main
import time
import psutil
import sys
from tkinter import messagebox, filedialog
from tkinter import ttk
from pathlib import Path

# Global variables
start_time = None
thread = None
# Get the current working directory
cwd = os.getcwd()
if r'windows' in cwd.lower():
    messagebox.showinfo("dick")
    cwd = str(Path.home())
    cwd += '\\Documents'

cwd.replace("\\", "/")  # Replace backslashes with forward slashes
cwd += "/"  # Add a trailing slash


def encode(max_threads, progress_var, cwd):
    global start_time
    start_time = time.time()
    file_path = filedialog.askopenfilename(
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("JPEG files", "*.jpeg"), ("BMP files", "*.bmp"), ("GIF files", "*.gif")]
    )
    thread = threading.Thread(
        target=main.encode, args=(file_path, max_threads, progress_var, cwd)
    )
    thread.start()
    return thread


def decode(max_threads, progress_var, cwd):
    global start_time
    start_time = time.time()
    thread = None

    files = filedialog.askopenfilenames(
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("JPEG files", "*.jpeg"), ("BMP files", "*.bmp"), ("GIF files", "*.gif")]
    )
    if len(files) == 2:
        to_decode_1 = files[0]
        to_decode_2 = files[1]
        thread = threading.Thread(
            target=main.decode,
            args=(to_decode_1, to_decode_2, max_threads, progress_var, cwd),
        )
    else:
        thread = threading.Thread(
            target=print(),
            args=("Please select two files for decoding."),
        )
        messagebox.showinfo("Error", "Please select two files for decoding.")
    thread.start()
    return thread


def start():
    global thread
    start_button.config(state="disabled")
    if mode.get() == "Encode":
        thread = encode(max_threads_value, progress_var, cwd)
    elif mode.get() == "Decode":
        thread = decode(max_threads_value, progress_var, cwd)
    else:
        messagebox.showinfo("Error", "Please select Encode or Decode.")
    if thread:
        window.after(1000, update_elapsed_time)


def enable_start_button():
    start_button.config(state="normal")


def update_elapsed_time():
    elapsed_time = time.time() - start_time
    if thread and thread.is_alive():
        elapsed_time_label.config(text=f"Elapsed Time: {int(elapsed_time)} seconds")
        window.after(1000, update_elapsed_time)
    else:
        if thread:
            thread.join()
        messagebox.showinfo("Info", f"Process completed in {elapsed_time:.2f} seconds.")
        enable_start_button()


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        current_pid = os.getpid()
        for proc in psutil.process_iter():
            if proc.pid == current_pid:
                proc.kill()
        window.destroy()


def open_cwd():
    global cwd
    if os.name == "nt":  # For Windows
        try:
            os.startfile(cwd + "/output")
        except FileNotFoundError:
            os.mkdir(cwd + "/output")
            os.startfile(cwd + "/output")
    elif os.name == "posix":  # For macOS and Linux
        os.system(f'open "{cwd}"' if sys.platform == "darwin" else f'xdg-open "{cwd}"')


# Create the main window
window = tk.Tk()
window.title("Visual Cryptography")
window.geometry("350x600")
window.minsize(160, 575)  # Set the minimal size of the window
# Set the global font
global_font = ("Helvetica", 12)

window.option_add("*Font", global_font)
# Instructions:
instructions = tk.Label(
    window,
    text="Upon pressing start you will be asked to choose the image."
    + "\nYou have to choose two images for decoding.",
    wraplength=320,
    justify="center",
)

instructions.pack(pady=10)
decoding_note = tk.Label(
    window,
    text="Decoding Note: The images must be of the same size and format.",
    wraplength=300,
    justify="center",
    font=("Arial", 10),
)
decoding_note.pack(pady=10)
# Image selection
image_label = tk.Label(window, text="Select Image:")
image_label.pack()

# Mode selection
mode = tk.StringVar()
mode.set("Encode")

encode_radio = tk.Radiobutton(window, text="Encode", variable=mode, value="Encode")
encode_radio.pack(pady=5)

decode_radio = tk.Radiobutton(window, text="Decode", variable=mode, value="Decode")
decode_radio.pack(pady=5)
# Threads instructions:
threads_instructions = tk.Label(
    window,
    text="Select the number of threads to use (1-15).\n"
    + "Don't use more threads than your CPU has.\n"
    + "If uncertain use the default value.",
    wraplength=300,
    justify="center",
    font=("Arial", 10),
)
threads_instructions.pack(pady=10)
# Max threads input
max_threads_label = tk.Label(window, text="Max Threads:")
max_threads_label.pack()

max_threads = tk.Entry(window, width=4)  # Set the width of the entry widget
max_threads.insert(0, "4")  # Set default value to 4
max_threads.pack()
try:
    max_threads_value = int(max_threads.get())
except ValueError:
    max_threads_value = 4
if not (max_threads_value > 0 and max_threads_value < 16):
    max_threads_value = 4

# Progress bar
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(
    window,
    variable=progress_var,
    maximum=100,
    mode="determinate",
)
progress_bar.pack(pady=10, fill=tk.X)

# Elapsed time label
elapsed_time_label = tk.Label(window, text="Elapsed Time: 0 seconds")
elapsed_time_label.pack()


# Start button
start_button = tk.Button(window, text="Start", command=start)
start_button.pack(pady=10)
# Folder structure
folder_structure = tk.Label(
    window,
    text="Program will create an output folder in the current working directory.",
    wraplength=300,
    justify="center",
    font=("Arial", 10),
)
folder_structure.pack(pady=10)
# Button to open current working directory
open_cwd_button = tk.Button(window, text="Open output folder", command=open_cwd)
open_cwd_button.pack(pady=10)

# Bind the closing event
window.protocol("WM_DELETE_WINDOW", on_closing)

# Start the main loop
window.mainloop()
