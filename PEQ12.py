from sympy import divisors

i=1
while True:
    x = int(i*(i+1)/2)
    if len(divisors(x)) == 500 or len(divisors(x)) > 500 :
        print(x)
        break
    i+=1
