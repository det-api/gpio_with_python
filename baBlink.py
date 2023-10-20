from pyA20.gpio import gpio
from pyA20.gpio import port
import time

# Set the GPIO pin number
led_pin = port.PA6  # You can use any available GPIO pin

# Initialize the GPIO library
gpio.init()

# Set up the GPIO pin as an output pin
gpio.setcfg(led_pin, gpio.OUTPUT)

try:
    while True:
        # Turn on the LED
        gpio.output(led_pin, gpio.HIGH)
        time.sleep(1)  # Wait for 1 second
        # Turn off the LED
        gpio.output(led_pin, gpio.LOW)
        time.sleep(1)  # Wait for 1 second

except KeyboardInterrupt:
    # Reset GPIO settings if the user interrupts the program
    gpio.cleanup()
