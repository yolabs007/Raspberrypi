# note if you are not aware of try and except concept, please use it now.
# it will be explained later on while we learn more code 


import RPi.GPIO as GPIO
import time

# Set up GPIO using BOARD numbering
GPIO.setmode(GPIO.BOARD)

# Set up the LED pin
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

# Set up PWM on the LED pin
led_pwm = GPIO.PWM(LED_PIN, 100)  # Frequency in Hz (100 Hz)

# Start PWM with 0% duty cycle (LED off)
led_pwm.start(0)

try:
    while True:
        # Increase brightness
        for duty_cycle in range(0, 101, 1):  # 0 to 100% in steps of 1%
            led_pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.02)  # Wait for 20ms

        # Decrease brightness
        for duty_cycle in range(100, -1, -1):  # 100 to 0% in steps of 1%
            led_pwm.ChangeDutyCycle(duty_cycle)
            time.sleep(0.02)  # Wait for 20ms

except KeyboardInterrupt:
    # Stop PWM
    led_pwm.stop()
    
    # Clean up GPIO
    GPIO.cleanup()
