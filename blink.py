import RPi.GPIO as GPIO
import time

# Set the GPIO pin number
led_pin = 11

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up the GPIO pin as an output pin
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        # Turn on the LED
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(1)  # Wait for 1 second
        # Turn off the LED
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    # Reset GPIO settings if the user interrupts the program
    GPIO.cleanup()
