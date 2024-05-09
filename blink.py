""" Your First Raspberry PI project 
Lets make one LED Blink 
Note: the pin number you selelcted varies based on 

GPIO.BOARD - pin numbers in orders as on board - reommended for starters or if you are going to use only one raspberry pi  

or GPIO.BCM - random gpio pin number based on chip   - for pro users

  by Rahul Sharma for Yolabs 
  This example code is in the public domain.
  https://www.yolabs.in
"""

import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering, please refer the pin diagram 
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

while True: # Run forever
  GPIO.output(8, GPIO.HIGH) # Turn on
  sleep(1) # Sleep for 1 second
  GPIO.output(8, GPIO.LOW) # Turn off
  sleep(1) # Sleep for 1 second
