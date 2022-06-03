import time

start_time = time.time()

def nextChain(number):
    result = 0
    digits = list(map(lambda x : int(x),list(str(number))))
    for digit in digits:
        result += pow(digit,2)
    return result

def allChain(value):
    while True:
        value = nextChain(value)
        if value == 1 or value == 89:
            return value     
i=1
count = 0
while True:
    print(i,allChain(i))
    if allChain(i)==89:
        count+=1
    if i == 10**7:
        break
    i+=1

print(f"Finally the result is {count}")
print("--- %s seconds ---" % (time.time() - start_time))