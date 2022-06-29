import time
start_time = time.time()

factorials = {0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880}
def factorialSum(number):
    total = 0
    for digit in str(number):
        total += factorials[int(digit)]
    return total

def factorialChain(n):
    chain = list()
    initial = n
    count = 0
    while True:
        n = factorialSum(n)
        if n in chain:
            return count+1
        chain.append(n)
        count +=1
        if n==initial:
            return count
n=3
count = 0
while n<10**6:
    if factorialChain(n)==60:
        count+=1
    n+=1
print(count)
print("--- %s seconds ---" % (time.time() - start_time))