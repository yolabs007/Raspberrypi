""" this is  as imple line follower code that works on  usb based camera.

known issues -  we will solve in line follower 2.0 
# 1. if a line is horizontal it sometimes fails to turn as the center of line is still in center of frame.
# 2. Vehicle is slow as turns is  not proportional turn and also sometimes  camera own shadow is detected as black area. 
# 3 . on ramp  currently vehicle is not balanced so we are not able to check willl check with 2.0 

"""

import cv2
import numpy as np
import time

from adafruit_servokit import ServoKit

############################
# CAMERA SETUP
############################
cap = cv2.VideoCapture(0)  # or your camera index

############################
# SERVOKIT SETUP
############################
kit = ServoKit(channels=16)

LEFT_SERVO_CHANNEL  = 0
RIGHT_SERVO_CHANNEL = 1

# The new 'zero' point for both servos
OFFSET = 0

############################
# HELPER: Set Both Wheels
############################
def set_wheels(left_final: float, right_final: float):
    """
    Directly write final throttle values 
    to the left and right servo channels.
    """
    kit.continuous_servo[LEFT_SERVO_CHANNEL].throttle  = left_final
    kit.continuous_servo[RIGHT_SERVO_CHANNEL].throttle = right_final

def stop_motors():
    """
    Both wheels at OFFSET => hopefully a true stop 
    if 0.2 is each servo's neutral.
    """
    set_wheels(OFFSET, OFFSET)

############################
# FORWARD/BACKWARD (Symmetrical about OFFSET)
############################
def drive(value: float):
    left_final  = 0.45
    right_final = -0.5
    set_wheels(left_final, right_final)

############################
# TURNING (Pivot)
############################
TURN_MAG = 0.4  # pivot speed (tweak as desired)

def turn_left():
    pivot_value = 0 - TURN_MAG
    set_wheels(pivot_value, pivot_value)


def turn_right():
    pivot_value = TURN_MAG
    set_wheels(pivot_value, pivot_value)
############################
# OPENCV LINE-FOLLOW LOGIC
############################
def preprocess_image(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(blurred, 100, 255, cv2.THRESH_BINARY_INV)
    return binary

def find_line_center(binary):
    height, width = binary.shape
    roi = binary[height // 2 : height, :]

    M = cv2.moments(roi)
    if M["m00"] > 0:
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"]) + (height // 2)
    else:
        cx, cy = width // 2, height // 2

    return cx, cy

def determine_direction(cx, frame_width):
    center = frame_width // 2
    offset = cx - center

    if abs(offset) < 40:
        return "FORWARD"
    elif offset > 40:
        return "RIGHT"
    else:
        return "LEFT"

############################
# MAIN LOOP
############################
try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to get frame.")
            break

        binary = preprocess_image(frame)
        cx, cy = find_line_center(binary)
        direction = determine_direction(cx, frame.shape[1])

        # Decide movement
        if direction == "FORWARD":
            drive(0.3)        # e.g. +0.3 => forward
        elif direction == "LEFT":
            turn_left()       # pivot left
        elif direction == "RIGHT":
            turn_right()      # pivot right

        # Optional debug
        cv2.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
        cv2.putText(frame, direction, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 
                    1, (0, 255, 0), 2)
        cv2.imshow("Binary", binary)
        cv2.imshow("Path", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Interrupted by user.")

finally:
    stop_motors()
    time.sleep(0.5)
    cap.release()
    cv2.destroyAllWindows()
    print("Program ended, motors stopped, camera released.")
