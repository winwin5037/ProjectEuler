import math

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
        primeFactors.add(int(n))
    return list(primeFactors)

def primePowers(n):
    powers = primefactors(n)
    count = 0
    results = list()
    for power in powers:
        while n%power==0:
            n = n/power
            count+=1
        results.append((power,count))
        count =0
    return sorted(results)

def h(a,b):
    c = 0
    if a==0:
        return 0
    while a%b==0:
        c+=1
        a = a/b
    return c

def fk(factorial,prime):
    r = 0
    for t in range(0,factorial+1,prime):
        r += h(t,prime)
    return r

def isprime(num):
    if num==2 or num==3:
        return True
    if num%2==0 or num<2:
        return False
    for n in range(3,int(num**0.5)+1,2):   
        if num%n==0:
            return False   
    return True

def s(n):
    if isprime(n):
        return n
    primes = primePowers(n)
    last = primes[-1][0]
    if math.factorial(last)%n==0:
        if math.factorial(last-1)%n!=0:
            return last
    else:
        pass