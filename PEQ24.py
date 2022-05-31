import itertools as it 
numbers = ["0","1","2","3","4","5","6","7","8","9"]

finalList = list(it.permutations(numbers))[1000000-1]
print("".join(finalList))