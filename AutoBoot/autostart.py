"""
Note: Name of main python file robotcode.py and also ensure the path is same else change the path in this code

if robotcode.py is crashed or stopped it can be started by preseeing the push pubton again 


"""
#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import subprocess

# GPIO pin for the Start Button
START_SWITCH_PIN = 17

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    # Use pull-up so pin reads HIGH normally, LOW when button is pressed
    GPIO.setup(START_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def wait_for_button_press():
    """
    Blocks until the button is pressed (pin goes LOW).
    """
    print("Waiting for the start button press...")
    while True:
        if GPIO.input(START_SWITCH_PIN) == GPIO.LOW:
            # Debounce or short delay
            time.sleep(0.2)
            # Optionally check if still LOW after short delay
            if GPIO.input(START_SWITCH_PIN) == GPIO.LOW:
                print("Start button pressed!")
                return
        time.sleep(0.1)

def run_robot_code():
    """
    Launch Robotcode.py as a subprocess, wait until it finishes (or crashes).
    """
    print("Launching Robotcode.py...")
    process = subprocess.Popen(["python3", "/home/pi/Robotcode.py"])
    # Wait for Robotcode.py to exit
    return_code = process.wait()
    print(f"Robotcode.py exited with code {return_code}")

def main():
    setup_gpio()

    # Main loop: wait for button, run code, repeat
    while True:
        # 1) Wait until user presses button
        wait_for_button_press()

        # 2) Run Robotcode.py
        run_robot_code()

        # 3) Once Robotcode.py finishes (or crashes),
        #    just loop back and wait for button again.
        #    No reboot required.

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()
        print("autostart.py exiting.")


