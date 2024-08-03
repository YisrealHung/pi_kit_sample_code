import RPi.GPIO as GPIO
import time

led = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
pwm = GPIO.PWM(led, 100)
pwm.start(0)
while True:
    for i in range(0,101,1):
        pwm.ChangeDutyCycle(i)
        time.sleep(0.01)
    for i in range(100,-1,-1):
        pwm.ChangeDutyCycle(i)
        time.sleep(0.01)