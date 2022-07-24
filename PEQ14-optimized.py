import time

start_time = time.time()

pastNumbers = dict()
def collatz(number,pastNumbers):
    m = number
    steps = 1
    while number!=1:
        if number in pastNumbers:
            steps += pastNumbers[number]-1
            break
        if number%2==0:
            number = number // 2
            steps+=1
        else:
            number = (number *3) +1
            steps +=1
    pastNumbers[m] = steps
    return steps

i=2
longestChain = 0
while True:
    temp = collatz(i,pastNumbers)
    if temp>longestChain:
        longestChain = temp
        maxNumber = i
    i+=1
    if i==10**6:
        break
print(maxNumber,longestChain)
print("--- %s seconds ---" % (time.time() - start_time))