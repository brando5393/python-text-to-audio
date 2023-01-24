import os
from tkinter import filedialog


class FileManager:
  """This class handles all interactions with the users file system"""

  def __init__(self):
    self.file_list = []  #contains all files that are selected for conversion
    self.download_directory = os.path.expanduser(
      "~")  #get the users home directory

  def add_files(self):
    """Add one or more files to the file list for conversion."""
    files_to_convert = filedialog.askopenfilenames()
    if files_to_convert != []:
      for file in files_to_convert:
        self.file_list.append(file)
        #display selected files in gui
        #log file selection complete
    else:
      #log files unable to be added
      #display error dialog
      pass

  def remove_file(self, file):
    """Remove a single file from the file list."""
    file_index = self.file_list.index(file)
    if file_index:
      self.file_list.pop(file_index)
    else:
      #log error to screen
      pass

  def clear_files(self):
    """Clear all files currently selected for conversion."""
    self.file_list.clear()
    #log to screen

  def set_download_directory(self):
    """Specify a new directory where audio files will be placed after conversion."""
    self.download_directory = filedialog.askdirectory()
    #update screen
