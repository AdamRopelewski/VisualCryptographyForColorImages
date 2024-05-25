import os
import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter import ttk
import threading
import main
import time
import psutil

# Global variables
start_time = None
thread = None
# Get the current working directory
cwd = os.getcwd()
cwd.replace("\\", "/")  # Replace backslashes with forward slashes
cwd += "/"  # Add a trailing slash


def encode(max_threads, progress_var, cwd):
    global start_time
    start_time = time.time()
    try:
        max_threads = int(max_threads)
    except ValueError:
        max_threads = 4
    if not (max_threads > 0 and max_threads < 16):
        max_threads = 4
    file_path = filedialog.askopenfilename(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
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
    try:
        max_threads = int(max_threads)
    except ValueError:
        max_threads = 4
    if not (max_threads > 0 and max_threads < 16):
        max_threads = 4
    files = filedialog.askopenfilenames(
        filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
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
    max_threads_value = max_threads.get()
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
                if "python" in proc.name():
                    proc.kill()
        window.destroy()


# Create the main window
window = tk.Tk()
window.title("Visual Cryptography")
window.geometry("400x350")

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

# Max threads input
max_threads_label = tk.Label(window, text="Max Threads:")
max_threads_label.pack()

max_threads = tk.Entry(window)
max_threads.insert(0, "4")  # Set default value to 4
max_threads.pack()

# Progress bar
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(
    window, variable=progress_var, maximum=100, mode="determinate"
)
progress_bar.pack(pady=10, fill=tk.X)

# Elapsed time label
elapsed_time_label = tk.Label(window, text="Elapsed Time: 0.00 seconds")
elapsed_time_label.pack()

# Start button
start_button = tk.Button(window, text="Start", command=start)
start_button.pack(pady=10)

# Bind the closing event
window.protocol("WM_DELETE_WINDOW", on_closing)

# Start the main loop
window.mainloop()
