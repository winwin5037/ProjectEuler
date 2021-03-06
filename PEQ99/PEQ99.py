import math
import time

start_time = time.time()

def f(a,b):
    return b*math.log(a,10)


with open("p099_base_exp.txt","r") as numbers:
    lines = numbers.readlines()

maxValue = 0
lineNumber = 1

for line in lines:
    line = line[:-1]
    inputList = line.split(",")
    a,b = int(inputList[0]),int(inputList[1])
    temp = f(a,b)
    if temp > maxValue:
        maxValue = temp
        answer = lineNumber
    lineNumber+=1

print(answer)
print("--- %s seconds ---" % (time.time() - start_time))
