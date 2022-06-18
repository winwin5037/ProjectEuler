import time
start_time = time.time()

def pentagon(n): return n*((3*n)-1)/2
i=6

PentagonList = [1,5,12,22,35]
while True:
    lastPentagon = pentagon(i)
    PentagonList.append(lastPentagon)
    for number in PentagonList:
        if lastPentagon - number in PentagonList:
            if abs(number-(lastPentagon-number)) in PentagonList:
                D = abs(number-(lastPentagon-number))
                print(D,number,lastPentagon-number)
                print("--- %s seconds ---" % (time.time() - start_time))
    i+=1
