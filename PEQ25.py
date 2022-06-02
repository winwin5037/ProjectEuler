def fibonacci(longer):
    F = [1,1,2]
    while not len(str(F[-1])) > longer -1:
        F.append(F[-2] + F[-1])
    return len(F)

fibonacci(1000)