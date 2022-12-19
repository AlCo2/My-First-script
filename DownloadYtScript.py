import tkinter as tk
from ctypes import windll
from tkinter import ttk
from tkinter.ttk import Label
from pytube import YouTube
from tkinter import messagebox
#window settings
windll.shcore.SetProcessDpiAwareness(1)
root = tk.Tk()
window_width = 800
window_height = 480
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.resizable(False, False)
root.iconbitmap('icon.ico')
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.title("Download")



#main app ============

ttk.Label(root, text="-----Download With Alco2(scorpio)-----").pack()


def error():
   messagebox.showerror('error', 'Error: error in lien!')


def onclick():
    try:
        youtubeObject = YouTube(url.get())
    except:
        error()
    choix1 = choix.get()
    if int(choix1)==1:
        youtubeObject = youtubeObject.streams.get_highest_resolution()
        try:
            youtubeObject.download(output_path="Video")
        except:
            error()
    elif int(choix1)==2:
        youtubeObject = youtubeObject.streams.get_audio_only()
        try:
            youtubeObject.download(output_path="Songs")
        except:
            error()
    messagebox.showinfo('Done', "download Done Successful")


choix = tk.StringVar()
r1 = ttk.Radiobutton(root, text="Video", variable=choix, value=1)
r1.pack(fill='x', padx=40)
r2 = ttk.Radiobutton(root, text="Music", variable=choix, value=2)
r2.pack(fill='x',pady=40, padx=40,)
url = tk.StringVar()
sendurl = ttk.Frame(root)
sendurl.pack( fill='x', pady=40, padx=40, expand=True)
url_entry = ttk.Entry(sendurl, textvariable=url)
url_entry.pack(fill='x', expand=True)
url_entry.focus()
send = ttk.Button(sendurl, text="Download", command=onclick)
send.pack(fill='x', expand=False, pady=10)



root.mainloop()