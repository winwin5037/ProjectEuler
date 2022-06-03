i,j = 0,2
finalList = list(range(1,10))

while True:
    if len(str(pow(i,j)))==j:
        print(i,j,i**j)
        finalList.append(i**j)
    i+=1
    if len(str(pow(i,j)))>j:
        i=0
        j+=1
        continue

# After the output 9 21 109418989131512359209 
# you will see that there is no more number which satisfies the condition
# so we can say that the answer is len(finalList) which is 49  

print(len(finalList))