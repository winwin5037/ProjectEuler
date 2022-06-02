def operation1(m,n):
    e = ""
    l1= list(range(1,n+1))
    for i in l1:
        e += str(m*i)
    return int(e)

def isdigit9(n):
    digitList = list(map(lambda x : int(x),list(str(n))))
    numbers = list(range(1,10))
    digitList.sort()
    if digitList == numbers:
        return True
    return False
    
finalList = list()

for i in range(2,10):
    for j in range(10**2,10**4):
        if isdigit9(operation1(j,i)):
            finalList.append(operation1(j,i))

print(max(finalList))