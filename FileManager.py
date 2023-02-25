import os
from tkinter import filedialog


class FileManager:
  """This class handles all interactions with the users file system"""

  def __init__(self, file_list_display, app_log_display,
               download_directory_label):
    self.file_list = []  # contains all files that are selected for conversion
    self.download_directory = os.path.expanduser(
      "~")  # get the user's home directory
    self.download_directory_label = download_directory_label  # reference to the label
    self.file_list_display = file_list_display  # reference to the label
    self.app_log_display = app_log_display
    self.download_directory_label.config(
      text=f"Current Download Directory: {self.download_directory}")

  def add_files(self):
    """Add one or more files to the file list for conversion."""
    files_to_convert = filedialog.askopenfilenames()
    if files_to_convert:
      for file in files_to_convert:
        self.file_list.append(file)
      # display selected files in gui
      # log file selection complete
    else:
      # log files unable to be added
      # display error dialog
      pass

  def remove_file(self):
    """Remove a single file from the file list."""
    try:
      self.file_list.remove()
    except ValueError:
      # log error to screen
      pass

  def clear_files(self):
    """Clear all files currently selected for conversion."""
    self.file_list.clear()
    # log to screen

  def set_download_directory(self):
    """Specify a new directory where audio files will be placed after conversion."""
    new_download_directory = filedialog.askdirectory()
    if new_download_directory:
      
      print(self.download_directory, new_download_directory)
      
      self.download_directory = new_download_directory
      # update the label with the new directory
      self.download_directory_label.config(
        text=f"Current Download Directory: {self.download_directory}")
    else:
      # log error to screen
      print("unable to change dir")