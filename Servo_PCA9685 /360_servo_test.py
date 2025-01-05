"""
Note: Generally servo may not have their zero match to software zero and you may need to find out  the actual value to stop.

Note: while servo need 5V-6V. VCC of PCA card is directly depends to the logic of board for example - for ESP & Raspberry pi - 3.3 V 

for arduino it is 5 V. 

Special Note:  in no circum stance plese short VCC and V+ both are differenrt  and having a very different purpose.  

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
