import tkinter as tk
import FileManager

explorer = FileManager.FileManager()

#create new instance of app
APP = tk.Tk()
#create the main application window
APP.geometry("960x540")
#prevent window resizing
#APP.resizable(0,0)
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
del_file_btn = tk.Button(APP, text="Remove File")
#place remove file button
del_file_btn.grid(row=2, column=1)
#create remove all files button
del_all_btn = tk.Button(APP,
                        text="Remove All Files",
                        command=explorer.clear_files)
#place remove all files button
del_all_btn.grid(row=3, column=1)

file_list_display = tk.Text(APP, height=15, width=15)

file_list_display.grid(row=1, column=0)
#create convert button
convert_btn = tk.Button(APP, text="Convert to Audio")
# place convert btn in window
convert_btn.grid(row=2, column=0)
download_directory_label = tk.Label(
  APP, text=f"Current Download Directory: {explorer.download_directory}")
download_directory_label.grid(row=3, column=0)
change_directory_button = tk.Button(APP,
                                    text="Change",
                                    command=explorer.set_download_directory)
change_directory_button.grid(row=3, column=1)
# create about button
about_btn = tk.Button(APP, text="About")
# place about button
# create exit button
exit_btn = tk.Button(APP, text="Exit")
# place exit button
# create log area
app_log_display = tk.Text(APP, height=10, width=20)
# place log area
#run application
APP.mainloop()
