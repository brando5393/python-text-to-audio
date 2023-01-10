import os, sys
import tkinter as tk


file_list = []

#create new instance of app
APP = tk.Tk()
#create the main application window
APP.geometry("312x324")
#prevent window resizing
APP.resizable(0,0)
#set window title
APP.title("Text to Audio Converter")
#create label for app header
app_header = tk.Label(APP, text="Text to Audio Converter")
#place header in window
app_header.pack()
#run application
APP.mainloop()