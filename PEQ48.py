def selfPower(n):
    result = 0
    for number in range(1,n):
       result += number**number
    return result % 10**10
print(selfPower(1001))