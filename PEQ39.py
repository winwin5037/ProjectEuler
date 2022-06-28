def perfectSquare(n):
    return pow(n,1/2)==int(pow(n,1/2))

def hypotenuse(c):
    results = list()
    if c%2==1:
        b = c
        while True:
            b -=2
            if perfectSquare(c*c-b*b):
                a = int((c*c-b*b)**0.5)
                results.append(tuple(sorted((a,b,c))))
            if b==1:
                break
    b=c
    while True:
            b -=1
            if perfectSquare(c*c-b*b):
                a = int((c*c-b*b)**0.5)
                results.append(tuple(sorted((a,b,c))))
            if b==1:
                break
    return set(results)

def frequency(A):
    f = 1
    for element in set(A):
        t = A.count(element)
        if t>f:
            print(t,element)
            f = t
            whichElement = element

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
