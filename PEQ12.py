import sympy as sp

finalList = list()
i=1
while True:
    x = int(i*(i+1)/2)
    if len(sp.divisors(x)) == 500 or len(sp.divisors(x)) > 500 :
        finalList.append(x)
    if len(finalList) == 1:
        break
    i+=1
print(finalList)