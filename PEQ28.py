import time

start_time = time.time()

starting = list()
n = 1002
total = 0
for i in range(1,n,2):
    starting.append(i*i)
    total+=i*i  # right up diagonal

for i in starting[1:]:
    # left up diagonal
    total += i-((i**(1/2))-1)

    # left down diagonal 
    total += i -((i**(1/2))-1) - i**(1/2) + 1

    # right down diagonal
    total += i -((i**(1/2))-1) - 2*i**(1/2) + 2

print(total)
print("--- %s seconds ---" % (time.time() - start_time))