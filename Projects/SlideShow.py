from itertools import cycle
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("Image Slideshow Viewer")

# List of image paths
image_paths = [
    r"C:\Users\shiva\OneDrive\Desktop\Images\Nayantara.webp",
    r"C:\Users\shiva\OneDrive\Desktop\Images\Disha.webp",
    r"C:\Users\shiva\OneDrive\Desktop\Images\Shreelila.webp",
    r"C:\Users\shiva\OneDrive\Desktop\Images\SanjanaImage.webp",
    r"C:\Users\shiva\OneDrive\Desktop\Images\Samntha.webp",
    r"C:\Users\shiva\OneDrive\Desktop\Images\Telugu3.jpg",
    r"C:\Users\shiva\OneDrive\Desktop\Images\Telugu4.jpg"

]

# Resize images
image_size = (1080, 1080)
images = [Image.open(path).resize(image_size) for path in image_paths]
photo_images = [ImageTk.PhotoImage(img) for img in images]

slideshow = cycle(photo_images)

label = tk.Label(root)
label.pack()

def update_image():
    photo = next(slideshow)
    label.config(image=photo)
    label.image = photo  # prevent garbage collection
    root.after(3000, update_image)  # 3 seconds

def start_slideshow():
    update_image()

play_button = tk.Button(root, text="Play Slideshow", command=start_slideshow)
play_button.pack(pady=10)

root.mainloop()

