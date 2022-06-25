import time

start_time = time.time()

def isprime(num):
    if num==2 or num==3:
        return True
    if num%2==0 or num<2:
        return False
    for n in range(3,int(num**0.5)+1,2):   
        if num%n==0:
            return False   
    return True

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

n = 2*3
maxValue = 0
nextPrime = 5
while True:
    if isprime(nextPrime):
        temp = n/totient(n)
        if temp > maxValue:
            maxValue = temp
            print(maxValue,n)
        if n>10**6:
            print("--- %s seconds ---" % (time.time() - start_time))
            break
    nextPrime += 2
