#https://projecteuler.net/problem=35

mainNumber = 10**6

import numpy as np
import time

start_time = time.time()

def digitelimination(n):
    results = np.array([])
    for i in n:
        if not ("8" in str(i) or "4" in str(i) or "6" in str(i) or "2" in str(i) or "5" in str(i) or "0" in str(i)):
            results = np.append(results,i)
    return results

transformint = lambda x : int(x)
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

primeNumbers = primer(mainNumber)
testList = transform(np.array(digitelimination(primeNumbers)))

finalList = np.array([2,3,5,7,11])
for i in testList:
    x = np.intersect1d(np.array(rotation(i)),primeNumbers)
    for j in x:
        if len(x) == len(rotation(i)):
            finalList = np.append(finalList,x)

print("--- %s seconds ---" % (time.time() - start_time))
print(f"The answer is {len(set(finalList))}")
