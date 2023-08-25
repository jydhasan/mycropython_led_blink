import machine
import time

# Set up the GPIO pin
led_pin = machine.Pin(2, machine.Pin.OUT)

try:
    while True:
        # Turn the LED on
        led_pin.on()
        time.sleep(5)  # Pause for 1 second

        # Turn the LED off
        led_pin.off()
        time.sleep(5)  # Pause for 1 second

except KeyboardInterrupt:
    pass
