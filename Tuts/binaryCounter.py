from machine import Pin
from time import sleep

four = Pin(12, Pin.OUT)
three = Pin(13, Pin.OUT)
two = Pin(14, Pin.OUT)
one = Pin(15, Pin.OUT)

lights = [four, three, two, one]


def toBinary(num):
    if num==1:
        return "1"
    elif num==0:
        return "0"
    
    return toBinary(num//2) + str(num%2)

def assignToLights(num):
    binValue = toBinary(num)
    while len(binValue) < 4:
        binValue = "0" + binValue
    
    for i in range(0, len(binValue)):
        lights[i].value(int(binValue[i]))


count = 0
while True:
    if count > 15:
        count = 0
    assignToLights(count)
    sleep(1)
    count+=1
