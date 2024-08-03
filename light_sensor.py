import RPi.GPIO as GPIO
import time

pir = 23

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pir,GPIO.IN)

while True:
    if GPIO.input(pir):
        print ("Light")

    else:
        print ("Dark")
    
    time.sleep(1)
        
