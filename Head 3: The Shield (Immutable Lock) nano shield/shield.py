Head 3: The Shield (Immutable Lock)
nano shield/shield.py

import os, time
def enforce_locks():
    ws_path = os.getcwd()
    os.system(f"sudo chattr +i {ws_path}/dna/*.py")
    os.system(f"sudo chattr +i {ws_path}/overwatch/*.py")
if __name__ == "__main__":
    while True:
        enforce_locks()
        time.sleep(60)
