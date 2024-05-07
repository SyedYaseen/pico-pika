# https://www.youtube.com/watch?v=ODWwErH_iGA&list=PLGs0VKk2DiYz8js1SJog21cDhkBqyAhC5&index=5&ab_channel=PaulMcWhorter
# Reading Analog Voltages Using a Potentiometer

from machine import Pin
from time import sleep

red=Pin(15, Pin.OUT)
yellow=Pin(14, Pin.OUT)
green=Pin(13, Pin.OUT)


def BitToVolts(potVal):
    x1=0 # min
    y1=192 # minimum of potentiometer

    # x2=3.3 #max volt
    x2=100 #max range
    y2=65535 #max pot
  
    # slope = (y2 - y1)/(x2 - x1)
    # Line eq: y-y1=m(x-x1)
    return (x2*(potVal-y1))/y2


potPin = 28
pot = machine.ADC(potPin)

while True:
    potVal = pot.read_u16()
    scaledPotVal=BitToVolts(potVal)
    print(scaledPotVal)

    if(scaledPotVal>0 and scaledPotVal<30):
        green.value(1)
        yellow.value(0)
        red.value(0)
    elif(scaledPotVal>30 and scaledPotVal<60):
        green.value(0)
        yellow.value(1)
        red.value(0)
    elif(scaledPotVal>60):
        green.value(0)
        yellow.value(0)
        red.value(1)

    
    sleep(0.4)




