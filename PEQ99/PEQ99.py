import math

def hmd(a,b):
    return math.floor(b*math.log(a,10))+1

with open("p099_base_exp.txt","r") as numbers:
    inputs = numbers.readlines()
    for line in inputs:
        line = line[:-1]
        inputList = line.split(",")
        a,b = int(inputList[0]),int(inputList[1])
        temp = hmd(a,b)
        if temp == 3005316:
            print([a,b,temp])
