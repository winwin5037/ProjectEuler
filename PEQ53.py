from math import comb
import time

start_time = time.time()

count = 0

for i in range(0,101):
    for j in range(0,i+1):
        if comb(i,j)>10**6:
            count+=1
print(count)
print("--- %s seconds ---" % (time.time() - start_time))