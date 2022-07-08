starting = list()
n = 1002
total = 0
# right up diagonal
for i in range(1,n,2):
    starting.append(i*i)
    total+=i*i
# left up diagonal
for i in starting[1:]:
    total += i-((i**(1/2))-1)
# left down diagonal
for i in starting[1:]:
    total += i -((i**(1/2))-1) - i**(1/2) + 1
# right down diagonal
for i in starting[1:]:
    total += i -((i**(1/2))-1) - 2*i**(1/2) + 1 + n - (n-1)

print(total)