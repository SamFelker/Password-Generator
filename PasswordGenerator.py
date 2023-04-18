import random
import string
import tkinter as tk
import pyperclip

def generate_password(length):
    """Generate a random password of specified length"""
    # Define the set of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a password by randomly selecting characters from the set
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate():
    """Generate a password of the specified length and display it in the GUI"""
    length = int(length_entry.get())
    password = generate_password(length)
    password_label.config(text=password)
    copy_button.config(state=tk.NORMAL)

def copy():
    """Copy the generated password to the clipboard"""
    password = password_label.cget('text')
    pyperclip.copy(password)

# Create the main window
window = tk.Tk()
window.title("Password Generator")
window.geometry("300x150")

# Create the widgets
length_label = tk.Label(window, text="Password length:")
length_entry = tk.Entry(window)
generate_button = tk.Button(window, text="Generate", command=generate)
copy_button = tk.Button(window, text="Copy", state=tk.DISABLED, command=copy)
password_label = tk.Label(window, text="Your password will appear here")

# Add the widgets to the window
length_label.pack()
length_entry.pack()
generate_button.pack()
copy_button.pack()
password_label.pack()

# Start the main event loop
window.mainloop()
