import math

def f(a,b):
    return math.floor(b*math.log(a,10))+1

with open("p099_base_exp.txt","r") as numbers:
    inputs = numbers.readlines()

maxValue = 0
finalList = list()

for line in inputs:
    line = line[:-1]
    inputList = line.split(",")
    a,b = int(inputList[0]),int(inputList[1])
    temp = f(a,b)
    finalList.append((a,b,temp))
    if temp > maxValue:
        maxValue = temp

for t in finalList:
    if t[2] == maxValue:
        print(t,finalList.index(t)+1)
