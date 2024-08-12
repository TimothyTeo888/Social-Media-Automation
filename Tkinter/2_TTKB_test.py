import tkinter as tk
import ttkbootstrap as tb
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
from tkcalendar import DateEntry
import datetime

class MediaSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Media Scheduler")
        self.root.geometry("800x600")  # Set a larger default window size

        # Create a frame for video display
        self.video_frame = tk.Frame(root)
        self.video_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Video Label
        self.video_label = tk.Label(self.video_frame)
        self.video_label.pack(fill=tk.BOTH, expand=True)

        # Create a frame for upload and schedule controls
        self.control_frame = tk.Frame(root)
        self.control_frame.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        # Upload Section
        self.upload_frame = tk.Frame(self.control_frame)
        self.upload_frame.pack(side=tk.LEFT, padx=5, pady=5)

        self.upload_button = tk.Button(self.upload_frame, text="Upload Media", command=self.upload_media)
        self.upload_button.pack(side=tk.LEFT)

        self.media_label = tk.Label(self.upload_frame, text="No media uploaded")
        self.media_label.pack(side=tk.LEFT, padx=5)

        # Date and Time Section
        self.schedule_frame = tk.Frame(self.control_frame)
        self.schedule_frame.pack(side=tk.RIGHT, padx=5, pady=5)

        self.date_label = tk.Label(self.schedule_frame, text="Select Date:")
        self.date_label.grid(row=0, column=0, padx=5)

        self.date_entry = DateEntry(self.schedule_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.date_entry.grid(row=0, column=1, padx=5)

        self.time_label = tk.Label(self.schedule_frame, text="Select Time:")
        self.time_label.grid(row=1, column=0, padx=5)

        self.time_entry = tk.Entry(self.schedule_frame, width=12)
        self.time_entry.grid(row=1, column=1, padx=5)

        self.schedule_button = tk.Button(self.schedule_frame, text="Schedule Post", command=self.schedule_post)
        self.schedule_button.grid(row=2, columnspan=2, pady=10)

        self.video_source = None
        self.video_cap = None

        # Bind the resize event
        self.root.bind("<Configure>", self.on_resize)

    def upload_media(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png"), ("Video Files", "*.mp4")])
        if file_path:
            self.file_path = file_path
            if file_path.lower().endswith(('.jpg', '.png')):
                self.display_image(file_path)
            elif file_path.lower().endswith('.mp4'):
                self.display_video(file_path)
            else:
                messagebox.showerror("Unsupported File", "Only images and mp4 videos are supported.")
            self.media_label.config(text=file_path.split('/')[-1])

    def display_image(self, file_path):
        try:
            image = Image.open(file_path)
            image = self.resize_image(image)
            self.img = ImageTk.PhotoImage(image)
            self.video_label.config(image=self.img)
        except Exception as e:
            messagebox.showerror("Error", f"Cannot display image: {e}")

    def display_video(self, file_path):
        self.video_source = file_path
        self.video_cap = cv2.VideoCapture(self.video_source)
        self.update_video_frame()

    def update_video_frame(self):
        if self.video_cap and self.video_cap.isOpened():
            ret, frame = self.video_cap.read()
            if ret:
                # Convert the frame to RGB
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                # Resize the frame to fit within the video frame while maintaining aspect ratio
                frame = self.resize_frame_to_fit(frame)
                # Convert the frame to ImageTk format
                self.img = ImageTk.PhotoImage(image=frame)
                self.video_label.config(image=self.img)
                self.video_label.after(30, self.update_video_frame)  # Schedule the next frame update
            else:
                self.stop_video()
        else:
            self.stop_video()

    def resize_frame_to_fit(self, frame):
        # Resize the frame to fit within the video player while maintaining aspect ratio
        image = Image.fromarray(frame)
        video_frame_width = self.video_frame.winfo_width()
        video_frame_height = self.video_frame.winfo_height()

        # Calculate new dimensions while maintaining aspect ratio
        img_width, img_height = image.size
        aspect_ratio = img_width / img_height

        if video_frame_width / video_frame_height > aspect_ratio:
            new_width = int(video_frame_height * aspect_ratio)
            new_height = video_frame_height
        else:
            new_width = video_frame_width
            new_height = int(video_frame_width / aspect_ratio)

        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        return image

    def resize_image(self, image):
        # Resize image to fit within the video frame while maintaining aspect ratio
        video_frame_width = self.video_frame.winfo_width()
        video_frame_height = self.video_frame.winfo_height()

        # Calculate new dimensions while maintaining aspect ratio
        img_width, img_height = image.size
        aspect_ratio = img_width / img_height

        if video_frame_width / video_frame_height > aspect_ratio:
            new_width = int(video_frame_height * aspect_ratio)
            new_height = video_frame_height
        else:
            new_width = video_frame_width
            new_height = int(video_frame_width / aspect_ratio)

        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
        return image

    def stop_video(self):
        if self.video_cap:
            self.video_cap.release()
        self.video_label.config(image='')

    def schedule_post(self):
        try:
            date = self.date_entry.get_date()
            time = self.time_entry.get()
            post_datetime = datetime.datetime.combine(date, datetime.datetime.strptime(time, '%H:%M').time())
            messagebox.showinfo("Scheduled", f"Post scheduled for {post_datetime}")
        except ValueError:
            messagebox.showerror("Error", "Invalid time format. Use HH:MM format.")

    def on_resize(self, event):
        # Resize the video player and update the video frame
        if self.video_cap and self.video_cap.isOpened():
            self.update_video_frame()

if __name__ == "__main__":
    root = tk.Tk()
    app = MediaSchedulerApp(root)
    root.mainloop()