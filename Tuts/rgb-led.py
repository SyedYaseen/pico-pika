from machine import Pin, PWM
from time import sleep
# My led is faulty :()
red=PWM(Pin(16))
green=PWM(Pin(17))
blue=PWM(Pin(18))
frequency=1000

red.freq(frequency)
green.freq(frequency)
blue.freq(frequency)
red.duty_u16(0)
green.duty_u16(0)
blue.duty_u16(0)

while True:
    red.duty_u16(65000)
    green.duty_u16(65000)
    blue.duty_u16(0)
    sleep(0.1)