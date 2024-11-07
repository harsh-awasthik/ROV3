import time
import pigpio

# Define the GPIO pin connected to the relay
RELAY_PIN = 17  # Change this to your GPIO pin

# Initialize pigpio library and connect to the daemon
pi = pigpio.pi()
if not pi.connected:
    print("Unable to connect to pigpio daemon")
    exit()

# Set up the relay pin as an output
pi.set_mode(RELAY_PIN, pigpio.OUTPUT)

def turn_relay_on():
    print("Turning relay ON")
    pi.write(RELAY_PIN, 0)  # Set the GPIO pin high (relay on)

def turn_relay_off():
    print("Turning relay OFF")
    pi.write(RELAY_PIN, 1)  # Set the GPIO pin low (relay off)

# Main logic to toggle relay
"""try:
    while True:
        turn_relay_on()
			
except KeyboardInterrupt:
	turn_relay_off()
	print("Program interrupted. Cleaning up...")
	pi.write(RELAY_PIN, 1)
	pi.stop()
"""
#finally:
    # Clean up the resources
    #pi.write(RELAY_PIN, 0)  # Ensure relay is off before exiting
    #pi.stop()  # Disconnect from the pigpio daemon
