import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

leds = [2, 3, 4, 17, 27, 22, 10, 9]

aux = [21, 20, 26, 16, 19, 25, 23, 24]

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)


GPIO.output(leds, 1)

while(True):
    for i in aux:
        GPIO.output(leds[aux.index(i)], GPIO.input(i))

GPIO.cleanup()