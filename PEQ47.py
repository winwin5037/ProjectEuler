import time
start_time = time.time()

def pf(n):
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
    return primeFactors
number = 2*3*5*7
while True:
    if len(pf(number))==4:
        number+=1
        if len(pf(number))==4:
            number+=1
            if len(pf(number))==4:
                number +=1
                if len(pf(number))==4:
                    print(number-3)
                    print("--- %s seconds ---" % (time.time() - start_time))
                    break
    number+=1
