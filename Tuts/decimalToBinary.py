one=0
two=0
three=0
four=0
lights = [one, two, three, four]
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
        lights[i]= int(binValue[i])
        


# print(toBinary(0))
assignToLights(15)
print(lights)