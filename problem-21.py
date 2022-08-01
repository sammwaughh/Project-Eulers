# Problem 21
import math

print("Running...")

isAmicableList = []

def divisorSum(n):
    divisorSum = 1
    sqrtN = math.sqrt(n)
    ceilSqrtN = math.ceil(sqrtN)
    for i in range(2, ceilSqrtN):
        if n % i == 0:
            divisorSum += i
            divisorSum += n // i
    if ceilSqrtN == sqrtN:
        divisorSum += sqrtN
            
    return divisorSum

def isAmicable(n):
    x = divisorSum(n)
    y = divisorSum(x)
    if n == y and n != x:
        return True
    else:
        return False


for i in range(3, 10000):
    if isAmicable(i):
        isAmicableList.append(i)

print(isAmicableList)
print(sum(isAmicableList))

print("...End")