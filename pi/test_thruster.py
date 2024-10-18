import pigpio
import time
import sys

t1 = 23
t2 = 24
t3 = 16
t4 = 21

thruster_pins = [t1, t2, t3, t4]

pi = pigpio.pi()

for item in thruster_pins:
    pi.set_servo_pulsewidth(item, 1500)

time.sleep(2)

duration = 60 * 5 # set time accordingly

start_time = time.time()

try:
    while time.time() - start_time() < duration:
        for item in thruster_pins:
            pi.set_servo_pulsewidth(item, 1550)
        
    print("Loop is running...")

except KeyboardInterrupt:
    print("\nKeyboardInterrupu caught, exiting...")

finally:
    for item in thruster_pins:
        pi.set_servo_pulsewidth(item, 1500)
            
    print("Values updated to Normal.")
    pi.stop()