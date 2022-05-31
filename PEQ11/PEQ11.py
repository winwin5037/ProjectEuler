import numpy as np
with open("file11.txt", "r") as f :
    data = f.readlines()
l1 = np.array([])
for i in data :
    s = i[:-1]
    l1 = np.append(l1,s.split(" "))
l1[-1] = 48
l1 = l1.reshape(20,20)

#right and left
results1 = np.array([])
for i in l1 :
    for x in range(len(i)-3):
        p1 = int(i[x]) * int(i[x+1]) * int(i[x+2]) * int(i[x+3])
        results1 = np.append(results1,p1)

#up and down
results2 = np.array([])
for i in range(17):
    for x in range(20):
        p2 = int(l1[i][x]) * int(l1[i+1][x]) * int(l1[i+2][x]) *int(l1[i+3][x])
        results2 = np.append(results2,p2)
        if p2 == 51267216:
            print(int(l1[i][x]), int(l1[i+1][x]), int(l1[i+2][x]), int(l1[i+3][x]))
        

#diagonal right
results3 = np.array([])
for i in range(17):
    for x in range(17):
        p3 = int(l1[i][x]) * int(l1[i+1][x+1]) * int(l1[i+2][x+2]) *int(l1[i+3][x+3])
        results3 = np.append(results3,p3)
#diagonal left
results4 = np.array([])
for i in range(17):
    for x in range(17):
        p4 = int(l1[i][x]) * int(l1[i+1][x-1]) * int(l1[i+2][x-2]) *int(l1[i+3][x-3])
        results4 = np.append(results4,p4)

finalResults = np.concatenate((results1,results2,results3,results4))

print(max(finalResults))