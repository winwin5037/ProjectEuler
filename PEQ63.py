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

# After the printed line 9 21 109418989131512359209, 
# you will see that there is no more output here
# because 10**n has n+1 digits and after this limit, 
# we cannot find any number which satisfies the condition
# so finally, the answer is len(finalList)
