import numpy as np

with open("peq13.txt","r") as number :
    n = number.readlines()

finalArray = np.array([])

for i in n :
    i = i[:-1]
    finalArray = np.append(finalArray,i)

finalArray[-1] = "53503534226472524250874054075591789781264330331690"
p = 0

for i in finalArray :
    i = int(i)
    p += i

    x = str(p)
print(x[:10])