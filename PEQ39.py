import time

start_time = time.time()

def perfectSquare(n):
    return pow(n,1/2)==int(pow(n,1/2))

def hypotenuse(c):
    results = list()
    b=c
    while True:
            b -=2
            if perfectSquare(c*c-b*b):
                a = int((c*c-b*b)**0.5)
                results.append(tuple(sorted((a,b,c))))
            if b<1:
                break
    return set(results)

def frequency(A):
    f = 1
    for element in set(A):
        temp = A.count(element)
        if temp>f:
            f = temp
            maxValue = element
    return maxValue

number = 5
results = list()

while True:
    if hypotenuse(number)==[]:
        number+=1
    for triangle in hypotenuse(number):
        if sum(triangle)<=1000:
            results.append(sum(triangle))
    number+=1
    if number>1000:
        break
print(frequency(results))
print("--- %s seconds ---" % (time.time() - start_time))