def isprime(num):
    if num==2 or num==3:
        return True
    if num%2==0 or num<2:
        return False
    for n in range(3,int(num**0.5)+1,2):   
        if num%n==0:
            return False   
    return True

def primerange(a,b):
    return filter(lambda x : isprime(x),range(a,b))
 
def isSquare(n):
    m = pow(n,1/2)
    return m == int(m)
    
def goldbach(n):
    for prime in primerange(3,n):
        if isSquare((n-prime)/2):
            return True
    return False
n = 33
while True:
    if isprime(n)==False:
        if goldbach(n)==False:
            print(n)
    n+=2