import itertools as it
import time

start_time = time.time()

numbers = ["0","1","2","3","4","5","6","7","8","9"]

finalList = list(it.permutations(numbers))[1000000-1]
print("".join(finalList))
print("--- %s seconds ---" % (time.time() - start_time))