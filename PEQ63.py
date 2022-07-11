import time

start_time = time.time()

i,j = 0,2
finalList = list(range(1,10))

while True:
    if len(str(pow(i,j)))==j:
        finalList.append(i**j)
    i+=1
    if len(str(pow(i,j)))>j or i==10:
        i=0
        j+=1
        continue
    if j>30:
        break
print(len(finalList))
print("--- %s seconds ---" % (time.time() - start_time))