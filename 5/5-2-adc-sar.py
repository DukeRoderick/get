import RPi.GPIO as GPIO
from time import sleep

dac  = [8, 11, 7,  1,  0,  5, 12, 6]
leds = [2,  3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.output(troyka, 1)

def dec2bin(a):
    return [(a >> i) & 1 for i in range(8)][::-1]

def adc():
    current = 0
    for i in range (7, -1, -1):
        print(current + (1<<i))
        print(dec2bin(current + (1<<i)))
        GPIO.output(dac, dec2bin(current + (1<<i)))
        sleep(0.01)
        print(GPIO.input(comp))
        if GPIO.input(comp) == 0:
            current += 1<<i
    return current

try:
    while True:
        a = (adc() + 1) // 32
        GPIO.output(leds, [1] * a + [0] * (8 - a))


finally:
    GPIO.output(dac,  0)
    GPIO.outout(leds, 0)
    GPIO.cleanup()import RPi.GPIO as GPIO
from time import sleep

dac  = [8, 11, 7,  1,  0,  5, 12, 6]
leds = [2,  3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.output(troyka, 1)

def dec2bin(a):
    return [(a >> i) & 1 for i in range(8)][::-1]

def adc():
    current = 0
    for i in range (7, -1, -1):
        print(current + (1<<i))
        print(dec2bin(current + (1<<i)))
        GPIO.output(dac, dec2bin(current + (1<<i)))
        sleep(0.01)
        print(GPIO.input(comp))
        if GPIO.input(comp) == 0:
            current += 1<<i
    return current

try:
    while True:
        n = adc()
        print(n, ' ~ ', f'{n/255 * 3.3} V')


finally:
    GPIO.output(dac,  0)
    GPIO.outout(leds, 0)
    GPIO.cleanup()
