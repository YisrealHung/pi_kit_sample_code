import time
import RPi.GPIO as GPIO

buzzer = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT)
pwm = GPIO.PWM(buzzer, 50)
pwm.start(50)

while True:
    print("Do")
    pwm.ChangeFrequency(523)
    time.sleep(1)

    print("Re")
    pwm.ChangeFrequency(587)
    time.sleep(1)
   
    print("Mi")
    pwm.ChangeFrequency(659)
    time.sleep(1)

    pwm.stop()
    time.sleep(3)