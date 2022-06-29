def collatz(n) :
    step = 0 
    while n!=1 :
        if n % 2 == 0 :
            n = n/2
            step += 1
        else:
            n = 3*n + 1 
            step +=1
    return step

i=2
longestChain = 0
while True:
    temp = collatz(i)
    if temp>longestChain:
        longestChain = temp
        longestNumber = i
    i+=1
    if i==10**6:
        break
print(longestNumber,longestChain)