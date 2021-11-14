import tkinter as tk, threading
import imageio
from PIL import Image, ImageTk
import os
from tkinter import *

video_name = "To_phir_aao.mp4" #This is your video file path
video = imageio.get_reader(video_name)

def stream(label):
    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image)
        label.image = frame_image

if __name__ == "__main__":
    root = tk.Tk()
    #my_label = tk.Label(root)
    #my_label.pack()
    img = ImageTk.PhotoImage(Image.open("pose_3.ppm"))
    panel = Label(root, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    thread = threading.Thread(target=stream, args=(my_label,))
    thread.daemon = 1
    thread.start()
    root.mainloop()