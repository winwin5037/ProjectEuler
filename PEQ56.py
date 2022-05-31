def digitSum(x):
    finalList = list()
    for i in list(str(x)):
        finalList.append(int(i))
    return sum(finalList)

powers = list()

for a in range(1,101):
    for b in range(1,101):
        powers.append(a**b)
    
print(max(map(lambda x : digitSum(x),X)))