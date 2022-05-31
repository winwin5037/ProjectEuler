def longer(n) :
    phase = 0 
    while n!=1 :
        if n % 2 == 0 :
            n = n/2
            phase += 1
        else:
            n = 3*n + 1 
            phase +=1
    return phase

rangeList = list(range(1,10**6))
collatzS = list(map(lambda x : longer(x),rangeList))
index = collatzS.index(max(collatzS))

print(rangeList[index])