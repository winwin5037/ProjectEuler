import numpy as np
import time

start_time = time.time()

def tri(n): return n*(n+1)/2
def penta(n): return n*(3*n -1)/ 2
def hexa(n): return n*(2*n -1)

rangeList = range(10**6)

tris = np.array(list(map(tri,rangeList)))
pentas = np.array(list(map(penta,rangeList)))
hexas = np.array(list(map(hexa,rangeList)))

results = np.intersect1d(np.intersect1d(tris,pentas),hexas)
print(results[-1])
print("--- %s seconds ---" % (time.time() - start_time))