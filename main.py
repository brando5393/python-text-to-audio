import tkinter as tk
from tkinter import messagebox, ttk

import Converter
import FileManager
from LogManager import LogManager

BG_COLOR = "#f4f5f7"
ACCENT_COLOR = "#2f6fed"


def confirm_quit():
    """Exits the app cleanly after yes/no prompt"""
    if messagebox.askyesno(title="Close Application", message="Are you sure you want to quit?"):
        app.destroy()


def build_style():
    style = ttk.Style(app)
    style.theme_use("clam")
    style.configure("TFrame", background=BG_COLOR)
    style.configure("TLabelframe", background=BG_COLOR, bordercolor="#d0d3d9")
    style.configure("TLabelframe.Label", background=BG_COLOR, font=("Segoe UI", 10, "bold"))
    style.configure("TLabel", background=BG_COLOR, font=("Segoe UI", 10))
    style.configure("Header.TLabel", background=BG_COLOR, font=("Segoe UI", 16, "bold"))
    style.configure("Directory.TLabel", background=BG_COLOR, font=("Segoe UI", 9), foreground="#555")
    style.configure("TButton", font=("Segoe UI", 10), padding=6)
    style.configure(
        "Accent.TButton",
        font=("Segoe UI", 10, "bold"),
        padding=8,
        background=ACCENT_COLOR,
        foreground="white",
    )
    style.map("Accent.TButton", background=[("active", "#255cc4")])
    return style


# Create the main application window
app = tk.Tk()
app.title("Text to Audio Converter")
app.geometry("820x600")
app.minsize(760, 560)
app.configure(background=BG_COLOR)

build_style()

# Header
header = ttk.Label(app, text="Text to Audio Converter", style="Header.TLabel")
header.grid(row=0, column=0, columnspan=2, sticky="w", padx=20, pady=(16, 8))

# Files section
files_frame = ttk.Labelframe(app, text="Files to Convert", padding=10)
files_frame.grid(row=1, column=0, sticky="nsew", padx=(20, 10), pady=8)

file_list_display = tk.Listbox(files_frame, height=14, activestyle="none", relief="flat", highlightthickness=1)
file_list_scroll = ttk.Scrollbar(files_frame, orient="vertical", command=file_list_display.yview)
file_list_display.configure(yscrollcommand=file_list_scroll.set)
file_list_display.grid(row=0, column=0, sticky="nsew")
file_list_scroll.grid(row=0, column=1, sticky="ns")
files_frame.rowconfigure(0, weight=1)
files_frame.columnconfigure(0, weight=1)

# Controls section
controls_frame = ttk.Labelframe(app, text="Actions", padding=10)
controls_frame.grid(row=1, column=1, sticky="new", padx=(10, 20), pady=8)

# Log section
log_frame = ttk.Labelframe(app, text="Activity Log", padding=10)
log_frame.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=20, pady=(8, 8))

app_log_display = tk.Listbox(
    log_frame, height=10, activestyle="none", relief="flat", highlightthickness=1, font=("Consolas", 9)
)
log_scroll = ttk.Scrollbar(log_frame, orient="vertical", command=app_log_display.yview)
app_log_display.configure(yscrollcommand=log_scroll.set)
app_log_display.grid(row=0, column=0, sticky="nsew")
log_scroll.grid(row=0, column=1, sticky="ns")
log_frame.rowconfigure(0, weight=1)
log_frame.columnconfigure(0, weight=1)

# Directory + exit bar
bottom_bar = ttk.Frame(app, padding=(20, 0, 20, 16))
bottom_bar.grid(row=3, column=0, columnspan=2, sticky="ew")
bottom_bar.columnconfigure(0, weight=1)

download_directory_label = ttk.Label(bottom_bar, style="Directory.TLabel")
download_directory_label.grid(row=0, column=0, sticky="w")

change_directory_button = ttk.Button(bottom_bar, text="Change Download Folder")
change_directory_button.grid(row=0, column=1, padx=(8, 8))

exit_btn = ttk.Button(bottom_bar, text="Exit", command=confirm_quit)
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

add_files_btn = ttk.Button(controls_frame, text="Add Files", command=explorer.add_files)
del_file_btn = ttk.Button(controls_frame, text="Remove Selected", command=explorer.remove_file)
del_all_btn = ttk.Button(controls_frame, text="Remove All", command=explorer.clear_files)
convert_btn = ttk.Button(
    controls_frame,
    text="Convert to Audio",
    style="Accent.TButton",
    command=lambda: converter.convert_to_audio(explorer.file_list),
)

add_files_btn.grid(row=0, column=0, sticky="ew", pady=(0, 6))
del_file_btn.grid(row=1, column=0, sticky="ew", pady=(0, 6))
del_all_btn.grid(row=2, column=0, sticky="ew", pady=(0, 18))
convert_btn.grid(row=3, column=0, sticky="ew")
controls_frame.columnconfigure(0, weight=1)

logger.add_event("info", "Application started successfully")

app.mainloop()
