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
    if isprime(nextPrime):
        n = n*nextPrime
        temp = n/eulerTotient(n)
        if temp > maxValue:
            maxValue = temp
            print(maxValue,n)
        if n>10**6:
            print("--- %s seconds ---" % (time.time() - start_time))
            break
    nextPrime += 2
