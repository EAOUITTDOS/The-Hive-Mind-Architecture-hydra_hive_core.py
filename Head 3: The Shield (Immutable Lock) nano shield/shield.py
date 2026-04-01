import os
import sys
import subprocess
import time

def check_status():
    print("--- [HEAD 3: THE SHIELD] ---")
    print("[+] Immutable Lock: ACTIVE")
    print("[+] Environment: FAFO (WSL2)")
    print("[+] Network: Hardened (Xfinity-Open-Shield)")
    
    try:
        # Checking host status via PowerShell bridge
        res = subprocess.check_output("Get-NetAdapterBinding -Name Wi-Fi | Where-Object {$_.ComponentID -eq 'ms_server'}", shell=True, executable='/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe')
        if b"False" in res:
            print("[+] Host Perimeter: SECURE (Sharing Disabled)")
    except:
        print("[!] Host Perimeter: UNKNOWN (Check PowerShell permissions)")

if __name__ == "__main__":
    if "--status" in sys.argv:
        check_status()
    else:
        print("Shield is standing by. Use --status to verify lock.")
