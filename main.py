import tkinter as tk
import FileManager

explorer = FileManager.FileManager()


def confirm_quit():
  """Exits the app cleanly after yes/no prompt"""
  answer = tk.messagebox.askyesno(title="Close Application",
                                  message="Are you sure you want to quit?")
  if answer == True:
    APP.destroy()
  else:
    pass


#create new instance of app
APP = tk.Tk()

#create the main application window
APP.geometry("960x540")

#prevent window resizing
APP.resizable(0, 0)

#set window title
APP.title("Text to Audio Converter")

#create label for app header
app_header = tk.Label(APP, text="Text to Audio Converter")

#place header in window
app_header.grid(row=0, column=0)

#create add files button
add_files_btn = tk.Button(APP, text="Add Files", command=explorer.add_files)

#place add files button
add_files_btn.grid(row=1, column=1)

#create reomve file button
del_file_btn = tk.Button(APP, text="Remove File", command=explorer.remove_file)

#place remove file button
del_file_btn.grid(row=2, column=1)

#create remove all files button
del_all_btn = tk.Button(APP,
                        text="Remove All Files",
                        command=explorer.clear_files)

#place remove all files button
del_all_btn.grid(row=3, column=1)

#create file list display
file_list_display = tk.Text(APP, height=15, width=15)

#place file list display
file_list_display.grid(row=1, column=0)

#create convert button
convert_btn = tk.Button(APP, text="Convert to Audio")

#place convert btn in window
convert_btn.grid(row=2, column=0)

#create download directory label
download_directory_label = tk.Label(
  APP, text=f"Current Download Directory: {explorer.download_directory}")

#place download_directory_label
download_directory_label.grid(row=5, column=0)

#create change dir button
change_directory_button = tk.Button(APP,
                                    text="Change",
                                    command=explorer.set_download_directory)

#place change_directory_button
change_directory_button.grid(row=5, column=1)

# create about button
about_btn = tk.Button(APP, text="About")

# place about button
about_btn.grid(row=4, column=0)

# create exit button
exit_btn = tk.Button(APP, text="Exit", command=confirm_quit)

# place exit button
exit_btn.grid(row=5, column=0)

# create log area
app_log_display = tk.Text(APP, height=10, width=20)

# place log area

#run application
APP.mainloop()
