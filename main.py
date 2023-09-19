import tkinter as tk
import FileManager
import Converter
import LogManager
from tkinter import messagebox

def confirm_quit():
  """Exits the app cleanly after yes/no prompt"""
  answer = messagebox.askyesno(title="Close Application",
                               message="Are you sure you want to quit?")
  if answer == True:
    app.destroy()
  else:
    pass


#create new instance of app
app = tk.Tk()
#create the main application window
app.geometry("800x600")
#prevent window resizing
app.resizable(0, 0)
#set window title
app.title("Text to Audio Converter")
# create frames
controls = tk.Frame(app)
main_display_area = tk.Frame(app)
directory_display = tk.Frame(app)
sub_display = tk.Frame(app)
# create label for app header
app_header = tk.Label(app, text="Text to Audio Converter")
#create file list display
file_list_display = tk.Listbox(main_display_area, height=15, width=25)
# create log area
app_log_display = tk.Listbox(sub_display, height=15, width=25)
#create download directory label
download_directory_label = tk.Label(directory_display)
#create new instance of FileManager
explorer = FileManager.FileManager(file_list_display, app_log_display,
                                   download_directory_label)
#create a new instance of Converter
converter=Converter.Converter()
#create convert button
convert_btn = tk.Button(main_display_area, text="Convert to Audio", command=converter.convert_to_audio(explorer.file_list))
#create add files button
add_files_btn = tk.Button(controls,
                          text="Add Files",
                          command=explorer.add_files)
#create reomve file button
del_file_btn = tk.Button(controls,
                         text="Remove File",
                         command=explorer.remove_file)
#create remove all files button
del_all_btn = tk.Button(controls,
                        text="Remove All Files",
                        command=explorer.clear_files)
#create change dir button
change_directory_button = tk.Button(directory_display,
                                    text="Change",
                                    command=explorer.set_download_directory)
# create exit button
exit_btn = tk.Button(app, text="Exit", command=confirm_quit)
# create about button
about_btn = tk.Button(app, text="About")
#place header in window
app_header.grid(row=0, column=0)

main_display_area.grid(row=1, column=0)

controls.grid(row=1, column=1)

directory_display.grid(row=2, column=0)

sub_display.grid(row=3, column=0)

#place file list display
file_list_display.grid(row=1, column=0)

#place convert btn in window
convert_btn.grid(row=2, column=0)

#place add files button
add_files_btn.grid(row=0, column=0)

#place remove file button
del_file_btn.grid(row=2, column=0)

#place remove all files button
del_all_btn.grid(row=3, column=0)

#place download_directory_label
download_directory_label.grid(row=4, column=0)

#place change_directory_button
change_directory_button.grid(row=4, column=1)

# place log area
app_log_display.grid(row=0, column=0)

# place about button

# place exit button
exit_btn.grid(row=4, column=2)

#logging testing
logger = LogManager.LogManager(app_log_display)
logger.add_event("info","log manager working", "200")

#run application
app.mainloop()
