def f(x,y):
    result = 0
    for i in list(str(x)):
        result += int(i)**y
    return result

final = 0

for i in range(2,10**6):
    if f(i,5) == i:
        final +=i
print(final)