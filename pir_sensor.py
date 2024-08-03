import RPi.GPIO as GPIO

pir = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir,GPIO.IN)

while True:
    if GPIO.input(pir):
        print ("Motion Not Detected")

    else:
        print ("Motion Detected")
        
