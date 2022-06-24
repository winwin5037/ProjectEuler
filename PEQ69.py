import time
start_time = time.time()

def isprime(n):
    if n<2:
        return False
    for i in range(2,int(n**(1/2))+1):
        if n%i==0:
            return False
    return True
        

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


n = 2*3
maxValue = 0
nextPrime = 5
while True:
    temp = n/eulerTotient(n)
    if temp > maxValue:
        maxValue = temp
        print(maxValue,n)
    if isprime(nextPrime):
        n = n*nextPrime
    if n>10**6:
        print("--- %s seconds ---" % (time.time() - start_time))
        break
    nextPrime += 2
