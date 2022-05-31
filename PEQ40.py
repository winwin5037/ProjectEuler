dc = "0.123"
numbers = [4]
for i in range(10**6):
    numbers.append(numbers[-1]+1)

for i in numbers:
    dc += str(i)

control = dc[2:]
product = 1

for i in [1,10,100,1000,10000,100000,1000000]:
    m = control[i-1]
    product *= int(m)

print(product)

