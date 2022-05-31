def op1(m,n):
    e = ""
    l1= list(range(1,n+1))
    for i in l1:
        e += str(m*i)
    return int(e)

def isdigit9(n):
    l1 = list(str(n))
    l2 = list()
    for i in l1:
        i = int(i)
        l2.append(i)
    numbers = list(range(1,10))
    l2.sort()
    if l2 == numbers:
        return True
    return False
    
finalList = list()

for i in range(2,10):
    for j in range(10**2,10**4):
        if isdigit9(op1(j,i)):
            finalList.append(op1(j,i))

print(max(finalList))