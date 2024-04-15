import os
from tkinter import filedialog
import LogManager as logger  # Add this import statement


class FileManager:
    """This class handles all interactions with the user's file system."""

    def __init__(self, file_list_display, app_log_display, download_directory_label):
        self.file_list = []  # Contains all files selected for conversion
        self.download_directory = os.path.expanduser("~")  # Get the user's home directory
        self.download_directory_label = download_directory_label  # Reference to the label
        self.file_list_display = file_list_display  # Reference to the listbox
        self.app_log_display = app_log_display
        self.logger = logger.LogManager(self.app_log_display)  # Use logger instead of LogManager
        self.download_directory_label.config(
            text=f"Current Download Directory: {self.download_directory}")

    def add_files(self):
        """Add one or more files to the file list for conversion."""
        try:
            files_to_convert = filedialog.askopenfilenames()
            if files_to_convert:
                for file in files_to_convert:
                    self.file_list.append(file)
                    filename = os.path.basename(file)
                    self.file_list_display.insert('end', filename)
                    index = self.file_list_display.size() - 1
                    self.file_list_display.itemconfigure(index, foreground='blue')
            else:
                # No files selected
                self.logger.add_event("warn", "No files selected for conversion", "")
        except Exception as e:
            self.logger.add_event("error", "Failed to add files for conversion", str(e))

    def remove_file(self):
        """Remove a single file from the file list."""
        try:
            selected_item = self.file_list_display.curselection()
            if selected_item:
                item_index = int(selected_item[0])
                self.file_list.pop(item_index)
                self.file_list_display.delete(item_index)
            else:
                # No file selected for removal
                self.logger.add_event("warn", "No file selected for removal", "")
        except Exception as e:
            self.logger.add_event("error", "Failed to remove file", str(e))

    def clear_files(self):
        """Clear all files currently selected for conversion."""
        try:
            self.file_list.clear()
            self.file_list_display.delete(0, 'end')
        except Exception as e:
            self.logger.add_event("error", "Failed to clear files", str(e))

    def set_download_directory(self):
        """Specify a new directory where audio files will be placed after conversion."""
        try:
            new_download_directory = filedialog.askdirectory()
            if new_download_directory:
                self.download_directory = new_download_directory
                # Update the label with the new directory
                self.download_directory_label.config(
                    text=f"Current Download Directory: {self.download_directory}")
            else:
                # No directory selected
                self.logger.add_event("warn", "No directory selected for download", "")
        except Exception as e:
            self.logger.add_event("error", "Failed to set download directory", str(e))
