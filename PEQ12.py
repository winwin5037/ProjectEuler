import sympy as sp

finalList = list()

for i in range(1,10**6):
    x = int(i*(i+1)/2)
    if len(sp.divisors(x)) == 500 or len(sp.divisors(x)) > 500 :
        finalList.append(x)
    if len(finalList) == 1:
        break
print(finalList)