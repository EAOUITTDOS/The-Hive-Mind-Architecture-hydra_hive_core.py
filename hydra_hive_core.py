import os
import multiprocessing
import time
import signal
import random

# --- THE HIVE REGISTRY ---
# Each 'Head' registers its Heartbeat here.
# If a Heartbeat stops, the Hive initiates 'Regrowth'.
shared_registry = multiprocessing.Manager().dict()

def head_logic(name, task_func):
    """The Logic for an individual Hydra Head."""
    while True:
        try:
            shared_registry[name] = time.time() # Update Heartbeat
            task_func()
            time.sleep(2)
        except Exception as e:
            print(f"[HIVE ALERT] Head {name} Compromised: {e}")
            break

def regrowth_monitor():
    """the 'Brain' that monitors the Hive for dead Heads."""
    while True:
        for head_name in ["Watcher", "Siphon", "Shield"]:
            last_heartbeat = shared_registry.get(head_name, 0)
            if time.time() - last_heartbeat > 5:
                print(f"[HIVE RESPAWN] {head_name} was cut. Regrowing 2 new instances...")
                # Logic to spawn a new process for the dead head
                spawn_head(head_name)
        time.sleep(1)

def spawn_head(name):
    # This is the 'Cut 1, Grow 2' logic
    p = multiprocessing.Process(target=head_logic, args=(name, lambda: print(f"Head {name} Active")))
    p.start()

if __name__ == "__main__":
    print("--- HIVE-MIND OVERWATCH INITIALIZED ---")
    # Start the Initial Heads
    for h in ["Watcher", "Siphon", "Shield"]:
        spawn_head(h)
    regrowth_monitor()
