import math
import numpy as np

finalList = np.array([])

for i in range(0,101):
    for j in range(0,i+1):
        finalList = np.append(finalList,math.comb(i,j))

print(len(finalList[finalList > 10**6]))