from machine import PWM, Pin
from time import sleep

def VoltsToBit(volts):
    # min of volt - 0 and min of 2^16 that represents is 65550
    # max of volt - 3.3 and max of 2^16 value - 65550
  
    # slope = (y2 - y1)/(x2 - x1)
    slope=65550/3.3
    # Line eq: y-y1=m(x-x1)
    return slope*volts

outLED=16
analogOut=PWM(Pin(outLED))

analogOut.freq(1000)
analogOut.duty_u16(0)

while True:
    volt=3.3
    bitValue=int(VoltsToBit(volt))
    analogOut.duty_u16(bitValue)
    sleep(0.1)
