#https://projecteuler.net/problem=35

mainNumber = 10**6

import numpy as np
import time

start_time = time.time()

def digitelimination(n):
    s2 = np.array([])
    for i in n:
        if "8" in str(i) or "4" in str(i) or "6" in str(i) or "2" in str(i) or "5" in str(i) or "0" in str(i):
            pass
        else:
            s2 = np.append(s2,i)
    return s2

def transformint(n): return int(n)
transform = np.vectorize(transformint)

def rotation(n):
    rotations = set()
    for i in range(len(str(n))):
        m = int(str(n)[i:] + str(n)[:i] )
        rotations.add(m)
    return list(rotations)

def primer(x):
        l , sieves = [], ([True]*x)
        for i in range(2,x):
            if sieves[i]:
                l.append(i)
                for j in range(i*i,x,i):
                    sieves[j] = False
        return np.array(l)

p = primer(mainNumber)
testList = np.array(list(range(mainNumber)))
testList = np.array(digitelimination(testList))
testList = transform(testList)
testList = testList[(testList%3 !=0) * (testList%7!=0) * (testList%11!=0)]

finalList = np.array([])
for i in testList:
    x = np.intersect1d(np.array(rotation(i)),p)
    for j in x:
        if len(x) == len(rotation(i)):
            finalList = np.append(finalList,x)
for i in [2,3,5,7,11]:
    finalList = np.append(finalList,i)
print("--- %s seconds ---" % (time.time() - start_time))
print(f"The answer is {len(set(finalList))}")