import datetime
import os

class LogManager:
    """This class performs logging functions for the application"""

    def __init__(self, app_log_display):
        self.app_log_display = app_log_display
        self.log_file_location = os.path.expanduser("~/texttoaudiopy.log")
        self._create_log_file()

    def _create_log_file(self):
        """Create log file if it doesn't exist"""
        if not os.path.isfile(self.log_file_location):
            try:
                with open(self.log_file_location, "w") as log_file:
                    log_file.write("=== Python Text To Audio Log ===\n")
            except Exception as e:
                self._log_to_display(f"ERROR: Unable to create log file at location {self.log_file_location} - {e}")

    def _log_to_display(self, message):
        """Log message to application display"""
        self.app_log_display.insert("end", f"[{datetime.datetime.now()}]: {message}\n")

    def add_event(self, status, msg, err):
        """Add an event to the application log file"""
        try:
            with open(self.log_file_location, "a") as log_file:
                log_file.write(f"[{datetime.datetime.now()}]: {status.upper()} | {msg.strip()} | {err.strip()}\n")
        except Exception as e:
            self._log_to_display(f"ERROR: Failed to log event - {e}")
