"""
This  code is for quic test for your continuous servo. 
Please look the picture for connections in the same folder 
Note: you must note connect VCC & V+ together both are having different purpose 
Connecting VCC to V+ will fry your raspberry pi and also may be the PCA card 

VCC -  3.3 V for ESP32, Raspberry pi or any board with 3.3V logic pins 
       5V for arduino or any board with 5V logic pins 

V+ -  Always 5-6 V this is for servo's  most of them run on 5V logic and need        

Note: Servos generally may not stop @ zero throttle  and may require a little bit tunning to arrive @ zero point 
for example in my case motors stopped @ 0.2 Throttle.  

"""




import time
from adafruit_servokit import ServoKit

# Create a ServoKit instance for a 16-channel PCA9685
kit = ServoKit(channels=16)

# Assume two continuous-rotation servos connected to channels 0 and 1
left_servo = kit.continuous_servo[0]
right_servo = kit.continuous_servo[1]

try:
    print("FORWARD for 2 seconds...")
    left_servo.throttle = 1.0    # full forward
    right_servo.throttle = 1.0
    time.sleep(2)

    print("STOP for 1 second...")
    left_servo.throttle = 0      # stop
    right_servo.throttle = 0
    time.sleep(1)

    print("REVERSE for 2 seconds...")
    left_servo.throttle = -1.0   # full reverse
    right_servo.throttle = -1.0
    time.sleep(2)

    print("STOP for 1 second...")
    left_servo.throttle = 0
    right_servo.throttle = 0
    time.sleep(1)

finally:
    # Always stop servos before exiting
    left_servo.throttle = 0
    right_servo.throttle = 0
    print("Done. Servos should be stopped now.")
