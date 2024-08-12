import tkinter as tk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class MediaSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Media Scheduler")
        self.root.geometry("800x600")  # Set a larger default window size
        
        h1_font = ("Roboto", 24)  # Corrected font definition
        h2_font = ("Roboto", 20)  # Corrected font definition
        h3_font = ("Roboto", 16)  # Corrected font definition

        # Create a parent frame to control layout
        self.main_frame = tb.Frame(self.root, padding=10)
        self.main_frame.pack(fill=tb.BOTH, expand=True)
    
        # Create a frame for video display
        self.video_frame = tb.Frame(self.main_frame, padding=1, bootstyle='primary')
        self.video_frame.pack(side=tb.RIGHT, fill=tb.BOTH, expand=True, ipadx=10)

        # Video Label
        self.video_label = tb.Label(self.video_frame)  # Use ttkbootstrap Label for consistency
        self.video_label.pack(fill=tb.BOTH, expand=True)

        # Create a frame for additional controls
        self.control_frame = tb.Frame(self.main_frame, padding=10, bootstyle='default')
        self.control_frame.pack(side=tb.LEFT, fill=tb.BOTH, expand=True, ipadx=10)

        # Add a title label
        self.control_label = tb.Label(self.control_frame, text="Media Scheduler", font=h1_font, bootstyle='default')
        self.control_label.grid(row=0, column=0, columnspan=2, pady=10, sticky='w')

        # Upload Section
        # Textbox to display the title of the media
        self.media_title_entry = tb.Entry(self.control_frame, width=30, bootstyle='light')
        self.media_title_entry.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

        # Upload button
        self.upload_button = tb.Button(self.control_frame, text="Upload Media", bootstyle='primary', command=self.upload_media)
        self.upload_button.grid(row=1, column=1, padx=5, pady=5)

    def upload_media(self):
        # Placeholder for media upload functionality
        # Update the media_title_entry with the media title after uploading
        media_title = "Sample Media Title"  # Replace with actual media title logic
        self.media_title_entry.delete(0, tk.END)
        self.media_title_entry.insert(0, media_title)

if __name__ == "__main__":
    root = tb.Window(themename="flatly")  # Create the main window with ttkbootstrap theme
    app = MediaSchedulerApp(root)
    root.mainloop()  # Call mainloop on the root window object
