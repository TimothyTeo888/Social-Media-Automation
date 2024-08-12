import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

counter = 0

def changer():
    global counter
    counter += 1
    if counter % 2 == 0:
        my_label.config(text="Hello World!")
    else:
        my_label.config(text="Goodbye World!")

# Create the main window with ttkbootstrap and darkly theme
root = tb.Window(themename="darkly")

# Define fonts
h1_font = ("Roboto", 28)
h2_font = ("Roboto", 20)

# Configure window title and size
root.title("TTK Bootstrap!")
root.geometry('500x350')

# Create and pack the label
my_label = tb.Label(root, text="Hello World", font=h1_font, bootstyle="default")
my_label.pack(padx=10, pady=10)

# Create and pack the button
my_button = tb.Button(root, text="Click Me", bootstyle="danger-outline", command=changer)
my_button.pack(pady=10)

# Start the main loop
root.mainloop()