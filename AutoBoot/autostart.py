#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import subprocess

# GPIO pin for the Start Button
START_SWITCH_PIN = 17

def wait_for_start_switch():
    GPIO.setmode(GPIO.BCM)
    # Use a pull-up, so pin reads HIGH by default, goes LOW when pressed
    GPIO.setup(START_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    print("System booted. Waiting for start button press...")
    
    # Wait until the button is pressed (pin goes LOW)
    while True:
        if GPIO.input(START_SWITCH_PIN) == GPIO.LOW:
            print("Button pressed! Launching main code...")
            break
        time.sleep(0.1)  # Debounce / poll time

def start_main_code():
    # Launch main_blink.py as a subprocess
    # The script will run until it's killed or Pi is turned off.
    subprocess.run(["python3", "/home/pi/main_blink.py"])  

if __name__ == "__main__":
    try:
        wait_for_start_switch()
        start_main_code()
    except KeyboardInterrupt:
        print("Listener interrupted.")
    finally:
        GPIO.cleanup()
        print("Listener script exiting.")
