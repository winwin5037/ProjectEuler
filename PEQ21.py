import numpy as np
import sympy as sp

def d(n) :
    x = np.array(sp.divisors(n))
    x = x[x<n]
    return sum(x)

rangeList = np.arange(1,10001)
finalArray = np.array([])

for i in rangeList :
    if d(d(i)) == i and i != d(i):
        finalArray = np.append(finalArray,i)
sum(finalArray)