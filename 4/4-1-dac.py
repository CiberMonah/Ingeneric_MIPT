import RPi.GPIO as GPIO

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

GPIO.setwarnings(False)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

try:
    while(True):

        num = input("Digital number: ")
        try:
            num = int(num)

            if 0 <= num <= 255:

                print(dec2bin(num))

                GPIO.output(dac, dec2bin(num))

                voltage = float(num) / 255.0 * 3.3

                print("Voltage is - ", voltage)

            elif num < 0:

                print("Number have to be more than zero")

            elif num > 255:

                print("Number have to be less than 256")

        except Exception:

            if num == "q": break
finally:

    GPIO.output(dac, 0)

    GPIO.cleanup()
    
    print("Program end") 