def f(a,b):
    result = ""
    for i in range(1,b+1):
        result += str(a*i)
    return int(result)

def isdigit9(n):
    return sorted(map(lambda x : int(x),list(str(n)))) == list(range(1,10))

maxValue = 0
for i in range(2,10):
    for j in range(10**2,10**4):
        temp = f(j,i)
        if isdigit9(temp):
            if temp > maxValue:
                maxValue = temp

print(maxValue)