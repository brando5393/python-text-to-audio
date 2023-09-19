import datetime
import os

class LogManager:
  """This class preformes logging functions for the application"""
  def __init__(self,app_log_display):
    self.app_log_display = app_log_display
    self.log_file_location = os.path.expanduser("~/texttoaudiopy.log")
    if os.path.isfile(self.log_file_location):
      pass
    else:
      try:
        with open(self.log_file_location, "w") as log_file:
          log_file.write("===Python Text To Audio Log===\n")
      except:
        self.app_log_display.insert("end",f"[{datetime.now()}]: WARN | Unable to create log file at locaton {self.log_file_location}")

  def add_event(self,status,msg,err):
    """Add an event to the application log file"""
    with open(self.log_file_location, "a") as log_file:
      log_file.write(f"[{datetime.now()}]: {status.toupper().strip()} | {msg.strip()} | {err.strip()}\n")

    
    