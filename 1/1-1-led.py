import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.IN)

