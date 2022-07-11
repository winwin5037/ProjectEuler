import time

start_time = time.time()

def divisors(n):
    for i in range(1, int(n/2) + 1):
        if n % i == 0:
            yield i
    yield n

def d(n):
    return sum(divisors(n))-n
i=2
total = 0
while True:
    if d(d(i))==i and i!=d(i):
        total +=i
    i+=1
    if i>10**4:
        break
print(total)
print("--- %s seconds ---" % (time.time() - start_time))