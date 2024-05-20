import keyboard
import time
import os

def detect_keylogger():
    print("Monitoring keyboard... Press 'esc' to exit.")
    while True:
      
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            key = event.name  
            print(f"Key pressed: {key}")
           
            if key == 'esc':
                print("Exiting keylogger detection.")
                break
           
detect_keylogger()

def check_for_keylogger():
    # Check for suspicious files in the current directory
    suspicious_files = ['Keylogger.exe', 'Keylogger.dll', 'Keylogger.py']
    for file in suspicious_files:
        if os.path.exists(file):
            print(f"Suspicious file found: {file}")
            return True
    return False

if check_for_keylogger():
    print("Keylogger detected!")
else:
    print("Keylogger not detected.")

detect_keylogger()
