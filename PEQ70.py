import time
start_time = time.time()

def primefactors(n):
    primeFactors = set()
    while n % 2 == 0:
        primeFactors.add(2)
        n = n / 2
    for i in range(3,int(n**(1/2))+1,2):
        while (n % i == 0):
            primeFactors.add(i)
            n = n / i
    if n > 2:
        primeFactors.add(n)
    return list(primeFactors)

def totient(n):
    factors = primefactors(n)
    result = n
    for factor in factors:
        result = result * (1-(1/factor))
    return int(result)

def permutation(a,b):
    return sorted(list(str(a))) == sorted(list(str(b)))

n=10**7+1
minValue = 2
while True:
    if permutation(n,totient(n)):
        temp = n/totient(n)
        if temp < minValue:
            minValue = temp
            print(n,temp)
            print("--- %s seconds ---" % (time.time() - start_time))
    n-=2
