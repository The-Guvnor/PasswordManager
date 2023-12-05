import tkinter as tk
from tkinter import ttk
import random
import string

def open_password_generator():
    # Function to open the password generator GUI
    import gui.py  # Assuming the previous GUI file is named password_generator_gui.py

# Create the main window
root = tk.Tk()
root.title("Main GUI")

# Set the dimensions of the window (width x height)
window_width = 300
window_height = 200
root.geometry(f"{window_width}x{window_height}")

# Button to open the password generator GUI
open_button = tk.Button(root, text="Open Password Generator", command=open_password_generator, font=("Arial", 12))
open_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Run the Tkinter event loop
root.mainloop()
