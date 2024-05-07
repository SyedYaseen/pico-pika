from machine import PWM, Pin
from time import sleep

potPin = 28
pot = machine.ADC(potPin)
outLED = 16
analogOut = PWM(Pin(outLED))

analogOut.freq(1000)
analogOut.duty_u16(0)

# while True:
#     analogOut.duty_u16(pot.read_u16())
#     sleep(0.01)

# Scale the pot values to 0-16 to clearly see differnce in  brightness
# The potval increases brightness linearly, we are scaling it to change exponentialy. Dont know why.
while True:
    potVal = pot.read_u16()
    expoVal = int((16/65535)*potVal)
    brightness = 2**expoVal

    print(potVal, expoVal, brightness)

    analogOut.duty_u16(2**expoVal)
    sleep(0.3)
