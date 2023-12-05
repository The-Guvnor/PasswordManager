import tkinter as tk
from tkinter import ttk
import random
import string
import pyperclip

def store_password(password):
    # Load the last 10 passwords from the file
    password_history = previous_passwords()

    # Add the current password to the list
    password_history.append(password)

    # Keep only the last 10 passwords
    password_history = password_history[-10:]

    # Save the updated list to the file
    with open("password_history.txt", "w") as file:
        for stored_password in password_history:
            file.write(stored_password + "\n")

def previous_passwords():
    try:
        with open("password_history.txt", "r") as file:
            # Read the last 10 passwords from the file
            password_history = file.read().splitlines()
    except FileNotFoundError:
        # Return an empty list if the file doesn't exist yet
        password_history = []
    return password_history

def password_strength(password_length):
    if 8 <= password_length <= 11:
        return "weak"
    elif 12 <= password_length <= 15:
        return "medium"
    elif password_length >= 16:
        return "strong"
    else:
        return ""

def generate_password():
    password_length = int(length_combobox.get())

    selected_options = [var.get() for var in checkboxes]

    uppercase_letters = string.ascii_uppercase if "A-Z" in selected_options else ""
    lowercase_letters = string.ascii_lowercase if "a-z" in selected_options else ""
    digits = string.digits if "0-9" in selected_options else ""
    special_characters = string.punctuation if "Special Characters" in selected_options else ""

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    password = ''.join(random.choice(all_characters) for _ in range(password_length))
    strength = password_strength(password_length)

    store_password(password)

    result_label.config(text=f"{password}")
    result_strength.config(text=f"Password strength: {strength}")

    if strength == "weak":
        result_strength.config(text=f"Password strength: {strength}", fg="lightcoral")
    elif strength == "medium":
        result_strength.config(text=f"Password strength: {strength}", fg="lightyellow")
    elif strength == "strong":
        result_strength.config(text=f"Password strength: {strength}", fg="lightgreen")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Set the dimensions of the window (width x height)
window_width = 400
window_height = 180
root.geometry(f"{window_width}x{window_height}")

# Disable window resizing
root.resizable(width=False, height=False)

# Label to display the generated password
result_label = tk.Label(root, text="", bg="lightblue", font=("Arial", 20), justify=tk.LEFT)
result_label.place(x=20, y=40, anchor=tk.W)

# Label to display the generated strength
result_strength = tk.Label(root, text="", font=("Arial", 8), justify=tk.LEFT)
result_strength.place(x=20, y=80, anchor=tk.W)

def copy_to_clipboard():
    # Copy the generated password to the clipboard
    generated_password = result_label.cget("text").strip()
    pyperclip.copy(generated_password)

# Button to copy to clipboard
copy_button = tk.Button(root, text="Copy", command=copy_to_clipboard, font=("Arial", 10))
copy_button.place(x=window_width - 90, y=40, anchor=tk.E)

# Button to generate password
generate_button = tk.Button(root, text="Generate", command=generate_password, font=("Arial", 10))
generate_button.place(x=window_width - 20, y=40, anchor=tk.E)

def load_password_history():
    # Load and display password history
    history_window = tk.Toplevel(root)
    history_window.title("Password History")
    # Set the dimensions of the window (width x height)
    window_width=260
    window_height=200
    history_window.geometry(f"{window_width}x{window_height}")
    # Disable window resizing
    history_window.resizable(width=False, height=False)

    # Load the last 10 passwords from the file
    password_history = previous_passwords()

    # Display the passwords in a listbox
    listbox = tk.Listbox(history_window, font=("Arial", 10))
    for password in password_history:
        listbox.insert(tk.END, password)
    listbox.pack(pady=10)

# Button to load password history
history_button = tk.Button(root, text="Password history", command=load_password_history, font=("Arial", 10))
history_button.place(x=window_width - 20, y=80, anchor=tk.E)

# Label for password length
length_label = tk.Label(root, text="Password length:", font=("Arial", 10))
length_label.place(x=20, y=110, anchor=tk.W)

# Combobox for password length
length_values = [str(i) for i in range(8, 25)]
length_combobox = ttk.Combobox(root, values=length_values, state="readonly", font=("Arial", 10), width=2)
length_combobox.set("8")
length_combobox.place(x=135, y=110, anchor=tk.W)

# Create and pack checkboxes for different options
checkboxes = [tk.StringVar(value="A-Z"), tk.StringVar(value="a-z"), tk.StringVar(value="0-9"),
              tk.StringVar(value="Special Characters")]
options = ["A-Z", "a-z", "0-9", "Special Characters"]

for i, option in enumerate(options):
    tk.Checkbutton(root, text=option, variable=checkboxes[i], onvalue=option, offvalue="", font=("Arial", 10)).place(
        x=20 + i * 60, y=140, anchor=tk.W)

# Generate a password upon launching the app
generate_password()

# Run the Tkinter event loop
root.mainloop()
