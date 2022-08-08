import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox
import shutil


def browse():
    download_dir = filedialog.askdirectory(initialdir="Your Directory Path")
    download_path.set(download_dir)

def download():
    url = video_link.get()
    folder = download_path.get()

    get_video = YouTube(url)
    get_stream = get_video.streams.first()
    get_stream.download(folder)

    messagebox.showinfo("Success","The Video Succesfully downloaded! You will find your video at\n" + folder)

screen = tk.Tk()
screen.geometry("800x450")
screen.title("Youtube Downloader")
screen.resizable(width=FALSE, height=FALSE)
screen.config(background="#B1BFDF")

download_path = StringVar()
video_link = StringVar()

Youtube_Label = Label(text="Youtube URL:", width=20, height=2, bg = "red", font=("ivy 13 bold"))
Youtube_Label.place(x=10,y=10)

Youtube_URL_Value = Entry(bg = "white", font=("ivy 20 bold"), textvariable=video_link)
Youtube_URL_Value.place(x=215,y=10)
Youtube_URL_Value.place(width=570,height=45)

Destination_Label = Label(text="Your Destination", width=20, height=2, bg = "red", font=("ivy 13 bold"))
Destination_Label.place(x=10,y=70)

Destination_Browse_Button = Button(text="Browse", width=19, height=2, bg = "white", font=("ivy 10 bold"), command=browse)
Destination_Browse_Button.place(x=620,y=70)


Destination_Entry = Entry(bg = "white", font=("ivy 13 bold"), textvariable=download_path)
Destination_Entry.place(width=400,height=45)
Destination_Entry.place(x=215,y=70)

Download_Button = Button(text="Download", width=19, height=2, bg = "Red", font=("ivy 18 bold"), command=download)
Download_Button.place(x=250,y=150)



screen.mainloop()
