import RPi.GPIO as GPIO
from time import sleep

# Define GPIO pins
sensor_pin = 14  # Replace with the actual GPIO pin connected to the sensor output
# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Set up sensor pin as input
GPIO.setup(sensor_pin, GPIO.IN)

try:
  # Infinite loop to continuously monitor sensor
  while True:
    # Read sensor state
    sensor_state = GPIO.input(sensor_pin)

    # Check if object is detected (sensor output is LOW)
    if sensor_state == GPIO.LOW:
      print("Object detected!")
    
    
    else:
      print("No object detected.")

finally:
  # Clean up GPIO on exit
  GPIO.cleanup()

print("Exiting...")
