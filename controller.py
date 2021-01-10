import RPi.GPIO as GPIO
import os

# Read data from Raspberry Pi (specifically read GPU temperature)
temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
print("GPU temperature is {}".format(temp[5:]))

# GPIO setup


# Turn on/off LED based on user input
try:
    while True:
        user_input = input("Turn LED On or Off with 1 or 0 (Ctrl-C to exit): ")
        if user_input is "1":
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(21,GPIO.OUT)
            GPIO.output(21,GPIO.HIGH)
            print("LED is on")
        elif user_input is "0":
            GPIO.output(21,GPIO.LOW)
            GPIO.cleanup()
            print("LED is off")
except KeyboardInterrupt:
    GPIO.cleanup()
    print("")