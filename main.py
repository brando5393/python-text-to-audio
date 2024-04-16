import tkinter as tk
from tkinter import messagebox
import FileManager
import Converter
import LogManager as logger

def confirm_quit():
    """Exits the app cleanly after yes/no prompt"""
    try:
        answer = messagebox.askyesno(title="Close Application",
                                     message="Are you sure you want to quit?")
        if answer:
            app.destroy()
    except Exception as e:
        log_manager.add_event("error", "Failed to close application", str(e))

# Create a new instance of the app
app = tk.Tk()

# Create the main application window
try:
    app.geometry("800x600")
    # Prevent window resizing
    app.resizable(0, 0)
    # Set window title
    app.title("Text to Audio Converter")
except Exception as e:
    logger.add_event("error", "Failed to set up main window", str(e))

# Create frames
try:
    controls = tk.Frame(app)
    main_display_area = tk.Frame(app)
    directory_display = tk.Frame(app)
    sub_display = tk.Frame(app)
except Exception as e:
    logger.add_event("error", "Failed to create frames", str(e))

# Create label for app header
try:
    app_header = tk.Label(app, text="Text to Audio Converter")
except Exception as e:
    logger.add_event("error", "Failed to create header label", str(e))

# Create file list display
try:
    file_list_display = tk.Listbox(main_display_area, height=15, width=25)
except Exception as e:
    logger.add_event("error", "Failed to create file list display", str(e))

# Create log area
try:
    app_log_display = tk.Listbox(sub_display, height=15, width=25)
except Exception as e:
    logger.add_event("error", "Failed to create log area", str(e))

# Create download directory label
try:
    download_directory_label = tk.Label(directory_display)
except Exception as e:
    logger.add_event("error", "Failed to create download directory label", str(e))

# Create new instance of LogManager
try:
    log_manager = logger.LogManager(app_log_display)
except Exception as e:
    logger.add_event("error", "Failed to initialize LogManager", str(e))

# Create a new instance of FileManager
try:
    explorer = FileManager.FileManager(file_list_display, app_log_display, download_directory_label)
except Exception as e:
    logger.add_event("error", "Failed to initialize FileManager", str(e))

# Create a new instance of Converter
try:
    converter = Converter.Converter()
except Exception as e:
    logger.add_event("error", "Failed to initialize Converter", str(e))

# Create convert button
try:
    convert_btn = tk.Button(main_display_area, text="Convert to Audio", command=lambda: converter.convert_to_audio(explorer.file_list))
except Exception as e:
    logger.add_event("error", "Failed to create convert button", str(e))

# Create add files button
try:
    add_files_btn = tk.Button(controls, text="Add Files", command=explorer.add_files)
except Exception as e:
    logger.add_event("error", "Failed to create add files button", str(e))

# Create remove file button
try:
    del_file_btn = tk.Button(controls, text="Remove File", command=explorer.remove_file)
except Exception as e:
    logger.add_event("error", "Failed to create remove file button", str(e))

# Create remove all files button
try:
    del_all_btn = tk.Button(controls, text="Remove All Files", command=explorer.clear_files)
except Exception as e:
    logger.add_event("error", "Failed to create remove all files button", str(e))

# Create change dir button
try:
    change_directory_button = tk.Button(directory_display, text="Change", command=explorer.set_download_directory)
except Exception as e:
    logger.add_event("error", "Failed to create change directory button", str(e))

# Create exit button
try:
    exit_btn = tk.Button(app, text="Exit", command=confirm_quit)
except Exception as e:
    logger.add_event("error", "Failed to create exit button", str(e))

# Place header in window
try:
    app_header.grid(row=0, column=0)
except Exception as e:
    logger.add_event("error", "Failed to place header in window", str(e))

# Place main display area in window
try:
    main_display_area.grid(row=1, column=0)
except Exception as e:
    logger.add_event("error", "Failed to place main display area in window", str(e))

# Place controls in window
try:
    controls.grid(row=1, column=1)
except Exception as e:
    logger.add_event("error", "Failed to place controls in window", str(e))

# Place directory display in window
try:
    directory_display.grid(row=2, column=0)
except Exception as e:
    logger.add_event("error", "Failed to place directory display in window", str(e))

# Place sub display in window
try:
    sub_display.grid(row=3, column=0)
except Exception as e:
    logger.add_event("error", "Failed to place sub display in window", str(e))

# Place file list display in window
try:
    file_list_display.grid(row=1, column=0)
except Exception as e:
    logger.add_event("error", "Failed to place file list display in window", str(e))

# Place convert button in window
try:
    convert_btn.grid(row=2, column=0)
except Exception as e:
    logger.add_event("error", "Failed to place convert button in window", str(e))

# Place add files button in window
try:
    add_files_btn.grid(row=0, column=0)
except Exception as e:
    logger.add_event("error", "Failed to place add files button in window", str(e))

# Place remove file button in window
try:
    del_file_btn.grid(row=2, column=0)
except Exception as e:
    logger.add_event("error", "Failed to place remove file button in window", str(e))

# Place remove all files button in window
try:
    del_all_btn.grid(row=3, column=0)
except Exception as e:
    logger.add_event("error", "Failed to place remove all files button in window", str(e))

# Place download directory label in window
try:
    download_directory_label.grid(row=4, column=0)
except Exception as e:
    logger.add_event("error", "Failed to place download directory label in window", str(e))

# Place change directory button in window
try:
    change_directory_button.grid(row=4, column=1)
except Exception as e:
    logger.add_event("error", "Failed to place change directory button in window", str(e))

# Place log area in window
try:
    app_log_display.grid(row=0, column=0)
except Exception as e:
    logger.add_event("error", "Failed to place log area in window", str(e))

# Place exit button in window
try:
    exit_btn.grid(row=4, column=2)
except Exception as e:
    logger.add_event("error", "Failed to place exit button in window", str(e))

# Logging testing
try:
    logger.add_event("info", "Application started successfully", "")
except Exception as e:
    logger.add_event("error", "Failed to log application start", str(e))

# Run the main loop
try:
    app.mainloop()
except Exception as e:
    logger.add_event("error", "Failed to start main loop", str(e))
