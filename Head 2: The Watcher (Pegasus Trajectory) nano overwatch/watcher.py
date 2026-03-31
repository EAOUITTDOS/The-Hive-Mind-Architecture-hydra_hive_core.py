Head 2: The Watcher (Pegasus Trajectory)
nano overwatch/watcher.py

import os, time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
HOME = os.path.expanduser("~")
LOG_FILE = os.path.join(HOME, "security_trajectory.csv")
class PegasusHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if not event.is_directory:
            with open(LOG_FILE, "a") as f:
                f.write(f"{time.time()}, {event.event_type}, {event.src_path}\n")
if __name__ == "__main__":
    observer = Observer()
    observer.schedule(PegasusHandler(), path=HOME, recursive=True)
    observer.start()
    while True: time.sleep(1)
