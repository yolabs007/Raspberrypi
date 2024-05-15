import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define the GPIO pins
motor_pin1 = 31  # GPIO6
motor_pin2 = 33  # GPIO13
motor_pin3 = 35  # GPIO19
motor_pin4 = 37  # GPIO26
proximity_sensor_pin = 21  # Choose an available GPIO pin
ground_pin = 39  # Ground

# Setup motor pins as output
GPIO.setup(motor_pin1, GPIO.OUT)
GPIO.setup(motor_pin2, GPIO.OUT)
GPIO.setup(motor_pin3, GPIO.OUT)
GPIO.setup(motor_pin4, GPIO.OUT)

# Setup proximity sensor pin as input
GPIO.setup(proximity_sensor_pin, GPIO.IN)

# Function to move forward
def move_forward():
    GPIO.output(motor_pin1, GPIO.HIGH)
    GPIO.output(motor_pin2, GPIO.LOW)
    GPIO.output(motor_pin3, GPIO.HIGH)
    GPIO.output(motor_pin4, GPIO.LOW)

# Function to stop
def stop():
    GPIO.output(motor_pin1, GPIO.LOW)
    GPIO.output(motor_pin2, GPIO.LOW)
    GPIO.output(motor_pin3, GPIO.LOW)
    GPIO.output(motor_pin4, GPIO.LOW)

try:
    while True:
        # Read the sensor value
        sensor_value = GPIO.input(proximity_sensor_pin)
        
        if sensor_value == GPIO.LOW:  # Assuming LOW means detection
            move_forward()
        else:
            stop()

        time.sleep(0.01)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
