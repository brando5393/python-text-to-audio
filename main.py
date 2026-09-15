import tkinter as tk
from tkinter import messagebox

import ttkbootstrap as ttk

import Converter
import FileManager
from LogManager import LogManager

# Swap "flatly" for "darkly" (or any other ttkbootstrap theme name) for a dark UI.
THEME = "flatly"


def confirm_quit():
    """Exits the app cleanly after yes/no prompt"""
    if messagebox.askyesno(title="Close Application", message="Are you sure you want to quit?"):
        app.destroy()


def styled_listbox(parent, **kwargs):
    """A tk.Listbox colored to match the current ttkbootstrap theme."""
    colors = style.colors
    return tk.Listbox(
        parent,
        activestyle="none",
        relief="flat",
        highlightthickness=1,
        highlightbackground=colors.border,
        highlightcolor=colors.primary,
        background=colors.inputbg,
        foreground=colors.inputfg,
        selectbackground=colors.primary,
        selectforeground=colors.selectfg,
        **kwargs,
    )


# Create the main application window
app = ttk.Window(title="Text to Audio Converter", themename=THEME, size=(860, 620), minsize=(760, 560))
style = ttk.Style()

# Header
header = ttk.Label(app, text="Text to Audio Converter", font=("Segoe UI", 18, "bold"))
header.grid(row=0, column=0, columnspan=2, sticky="w", padx=20, pady=(18, 10))

# Files section
files_frame = ttk.Labelframe(app, text="Files to Convert", padding=10, bootstyle="primary")
files_frame.grid(row=1, column=0, sticky="nsew", padx=(20, 10), pady=8)

file_list_display = styled_listbox(files_frame, height=14)
file_list_scroll = ttk.Scrollbar(files_frame, orient="vertical", command=file_list_display.yview, bootstyle="round")
file_list_display.configure(yscrollcommand=file_list_scroll.set)
file_list_display.grid(row=0, column=0, sticky="nsew")
file_list_scroll.grid(row=0, column=1, sticky="ns")
files_frame.rowconfigure(0, weight=1)
files_frame.columnconfigure(0, weight=1)

# Controls section
controls_frame = ttk.Labelframe(app, text="Actions", padding=10, bootstyle="primary")
controls_frame.grid(row=1, column=1, sticky="new", padx=(10, 20), pady=8)

# Log section
log_frame = ttk.Labelframe(app, text="Activity Log", padding=10, bootstyle="secondary")
log_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=20, pady=(8, 8))

app_log_display = styled_listbox(log_frame, height=10, font=("Consolas", 9))
log_scroll = ttk.Scrollbar(log_frame, orient="vertical", command=app_log_display.yview, bootstyle="round")
app_log_display.configure(yscrollcommand=log_scroll.set)
app_log_display.grid(row=0, column=0, sticky="nsew")
log_scroll.grid(row=0, column=1, sticky="ns")
log_frame.rowconfigure(0, weight=1)
log_frame.columnconfigure(0, weight=1)

# Directory + exit bar
bottom_bar = ttk.Frame(app, padding=(20, 0, 20, 16))
bottom_bar.grid(row=3, column=0, columnspan=2, sticky="ew")
bottom_bar.columnconfigure(0, weight=1)

download_directory_label = ttk.Label(bottom_bar, bootstyle="secondary")
download_directory_label.grid(row=0, column=0, sticky="w")

change_directory_button = ttk.Button(bottom_bar, text="Change Download Folder", bootstyle="secondary-outline")
change_directory_button.grid(row=0, column=1, padx=(8, 8))

exit_btn = ttk.Button(bottom_bar, text="Exit", command=confirm_quit, bootstyle="danger-outline")
exit_btn.grid(row=0, column=2)

app.columnconfigure(0, weight=3)
app.columnconfigure(1, weight=1)
app.rowconfigure(1, weight=1)
app.rowconfigure(2, weight=1)

# Wire up the app's logic
logger = LogManager(app_log_display)
explorer = FileManager.FileManager(file_list_display, app_log_display, download_directory_label)
converter = Converter.Converter(app_log_display)
change_directory_button.configure(command=explorer.set_download_directory)

add_files_btn = ttk.Button(controls_frame, text="Add Files", command=explorer.add_files, bootstyle="primary")
del_file_btn = ttk.Button(
    controls_frame, text="Remove Selected", command=explorer.remove_file, bootstyle="secondary-outline"
)
del_all_btn = ttk.Button(
    controls_frame, text="Remove All", command=explorer.clear_files, bootstyle="secondary-outline"
)
convert_btn = ttk.Button(
    controls_frame,
    text="Convert to Audio",
    bootstyle="success",
    command=lambda: converter.convert_to_audio(explorer.file_list),
)

add_files_btn.grid(row=0, column=0, sticky="ew", pady=(0, 6))
del_file_btn.grid(row=1, column=0, sticky="ew", pady=(0, 6))
del_all_btn.grid(row=2, column=0, sticky="ew", pady=(0, 18))
convert_btn.grid(row=3, column=0, sticky="ew", ipady=4)
controls_frame.columnconfigure(0, weight=1)

logger.add_event("info", "Application started successfully")

app.mainloop()
