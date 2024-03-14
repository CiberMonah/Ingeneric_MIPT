import RPi.GPIO as GPIO
import time

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

num = 0
mode = True
T = 5
repeats = 5
counter = 0

try:
    while(counter <= repeats):
        GPIO.output(dac, dec2bin(num))
        
        if mode:
            num = num + 1
        else:
            num = num - 1

        time.sleep(T / 512)

        if num == 255:
            mode = False
            counter = counter + 1
        if num == 0:
            mode = True

        
            
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("Program end") 