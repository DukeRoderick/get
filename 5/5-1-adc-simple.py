import RPi.GPIO as GPIO
from time import sleep

dac  = [8, 11, 7,  1,  0,  5, 12, 6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.output(troyka, 1)

def dec2bin(a):
    return [(a >> i) & 1 for i in range(8)][::-1]

def adc():
    current = 0
    for i in range (255, -1, -1):
        GPIO.output(dac, dec2bin(i))
        sleep(0.01)
        if GPIO.input(comp) == 0:
            current = i
            break
    return current

try:
    while True:
        print(3.3 * (adc() / 255), 'V')

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
