import time
from sympy import isprime
start_time = time.time()

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def eulerTotient(n):
    result = 1
    if n%2==0:
        for i in range(3,n,2):
            if gcd(i,n)==1:
                result +=1
    else:
        for i in range(2,n):
            if gcd(i,n)==1:
                result +=1
    return result

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

# I defined two functions here and if you prefer to use totient() function, you will notice that it's much more efficient.

n = 2*3
maxValue = 0
nextPrime = 5
while True:
    temp = n/totient(n)
    if temp > maxValue:
        maxValue = temp
        print(maxValue,n)
    if isprime(nextPrime):
        n = n*nextPrime
    if n>10**6:
        print("--- %s seconds ---" % (time.time() - start_time))
        break
    nextPrime += 2
