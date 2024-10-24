import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera

# Set up the GPIO
GPIO.setmode(GPIO.BCM)
l1 = 6  # Change this to your desired GPIO pin number
GPIO.setup(l1, GPIO.IN)

# Initialize camera
camera = PiCamera()
camera.resolution = (720, 1280)

count = 0

try:
    while True:
        a = GPIO.input(l1)
        if a == 0:  # Assuming active low signal
            count += 1
            print(f"Taking picture {count}")
            
            camera.start_preview()
            sleep(2)  # Give the camera time to adjust
            camera.capture(f'/home/pi/Desktop/183410/image_{count}.jpg')
            camera.stop_preview()
            
            sleep(1)  # Debounce delay to prevent multiple captures
except KeyboardInterrupt:
    print("Exiting program.")
finally:
    GPIO.cleanup()  # Clean up GPIO on exit
    camera.close()  # Close camera when done
