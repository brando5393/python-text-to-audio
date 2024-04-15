import tkinter as tk
from tkinter import messagebox
import FileManager
import Converter
import LogManager as logger

# Define a function to confirm quitting the application
def confirm_quit():
    try:
        # Display a yes/no prompt to confirm quitting
        answer = messagebox.askyesno(title="Close Application", message="Are you sure you want to quit?")
        if answer:
            app.destroy()  # If yes, destroy the application window
    except Exception as e:
        # Log any errors that occur during the process
        logger.add_event("error", "Failed to close application", str(e))

# Create a new instance of the Tkinter application
app = tk.Tk()

try:
    # Set the size and title of the main application window
    app.geometry("800x600")
    app.resizable(0, 0)  # Prevent window resizing
    app.title("Text to Audio Converter")
except Exception as e:
    # Log any errors that occur during window setup
    logger.add_event("error", "Failed to set up main window", str(e))

# Create frames for organizing the layout
try:
    controls = tk.Frame(app)
    main_display_area = tk.Frame(app)
    directory_display = tk.Frame(app)
    sub_display = tk.Frame(app)
except Exception as e:
    # Log any errors that occur during frame creation
    logger.add_event("error", "Failed to create frames", str(e))

# Create a label for the application header
try:
    app_header = tk.Label(app, text="Text to Audio Converter")
except Exception as e:
    # Log any errors that occur during label creation
    logger.add_event("error", "Failed to create header label", str(e))

# Create a listbox for displaying the file list
try:
    file_list_display = tk.Listbox(main_display_area, height=15, width=25)
except Exception as e:
    # Log any errors that occur during listbox creation
    logger.add_event("error", "Failed to create file list display", str(e))

# Create a listbox for displaying log messages
try:
    app_log_display = tk.Listbox(sub_display, height=15, width=25)
except Exception as e:
    # Log any errors that occur during listbox creation
    logger.add_event("error", "Failed to create log area", str(e))

# Create a label for displaying the download directory
try:
    download_directory_label = tk.Label(directory_display)
except Exception as e:
    # Log any errors that occur during label creation
    logger.add_event("error", "Failed to create download directory label", str(e))

# Initialize the FileManager instance
try:
    explorer = FileManager.FileManager(file_list_display, app_log_display, download_directory_label)
except Exception as e:
    # Log any errors that occur during FileManager initialization
    logger.add_event("error", "Failed to initialize FileManager", str(e))

# Initialize the Converter instance
try:
    converter = Converter.Converter()
except Exception as e:
    # Log any errors that occur during Converter initialization
    logger.add_event("error", "Failed to initialize Converter", str(e))

# Create a button for converting files to audio
try:
    convert_btn = tk.Button(main_display_area, text="Convert to Audio", command=lambda: converter.convert_to_audio(explorer.file_list))
except Exception as e:
    # Log any errors that occur during button creation
    logger.add_event("error", "Failed to create convert button", str(e))

# Create a button for adding files
try:
    add_files_btn = tk.Button(controls, text="Add Files", command=explorer.add_files)
except Exception as e:
    # Log any errors that occur during button creation
    logger.add_event("error", "Failed to create add files button", str(e))

# Create a button for removing files
try:
    del_file_btn = tk.Button(controls, text="Remove File", command=explorer.remove_file)
except Exception as e:
    # Log any errors that occur during button creation
    logger.add_event("error", "Failed to create remove file button", str(e))

# Create a button for removing all files
try:
    del_all_btn = tk.Button(controls, text="Remove All Files", command=explorer.clear_files)
except Exception as e:
    # Log any errors that occur during button creation
    logger.add_event("error", "Failed to create remove all files button", str(e))

# Create a button for changing the download directory
try:
    change_directory_button = tk.Button(directory_display, text="Change", command=explorer.set_download_directory)
except Exception as e:
    # Log any errors that occur during button creation
    logger.add_event("error", "Failed to create change directory button", str(e))

# Create a button for exiting the application
try:
    exit_btn = tk.Button(app, text="Exit", command=confirm_quit)
except Exception as e:
    # Log any errors that occur during button creation
    logger.add_event("error", "Failed to create exit button", str(e))

# Place the application components in the layout
try:
    app_header.grid(row=0, column=0)  # Place the header label
    main_display_area.grid(row=1, column=0)  # Place the main display area
    controls.grid(row=1, column=1)  # Place the control buttons
    directory_display.grid(row=2, column=0)  # Place the download directory display
    sub_display.grid(row=3, column=0)  # Place the log display
    file_list_display.grid(row=1, column=0)  # Place the file list display
    convert_btn.grid(row=2, column=0)  # Place the convert button
    add_files_btn.grid(row=0, column=0)  # Place the add files button
    del_file_btn.grid(row=2, column=0)  # Place the remove file button
    del_all_btn.grid(row=3, column=0)  # Place the remove all files button
    download_directory_label.grid(row=4, column=0)  # Place the download directory label
    change_directory_button.grid(row=4, column=1)  # Place the change directory button
    app_log_display.grid(row=0, column=0)  # Place the log area
    exit_btn.grid(row=4, column=2)  # Place the exit button
except Exception as e:
    # Log any errors that occur during layout placement
    logger.add_event("error", "Failed to place components in window", str(e))

# Test LogManager functionality by logging an event
try:
    log_manager = logger.LogManager(app_log_display)
    log_manager.add_event("info", "Log manager working", "200")
except Exception as e:
    # Log any errors that occur during LogManager initialization
    logger.add_event("error", "Failed to initialize LogManager", str(e))

# Run the application
try:
    app.mainloop()
except Exception as e:
    # Log any errors that occur during application execution
    logger.add_event("error", "Failed to run application", str(e))
