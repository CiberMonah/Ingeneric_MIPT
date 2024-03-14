import RPi.GPIO as GPIO

pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 1000)
p.start(0)
f = 0

try:
    while True:
        f =float(input())
        p.ChangeDutyCycle(f)
        print(3.3 * f / 100.0)

finally:
    p.stop()
    GPIO.output(pin, 0)
    GPIO.cleanup()