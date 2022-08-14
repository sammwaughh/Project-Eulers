# Problem 23
import math

print("Running...")

def isAbundant(n):
    divisorSum = 1
    for i in range(2, math.floor(math.sqrt(n))+1):
        if n % i == 0:
            divisorSum += i
            otherFactor = n//i
            if otherFactor != i:
                divisorSum += otherFactor
    if divisorSum > n:
        return True
    else:
        return False

abundants = []
for i in range(1, 28124):
    if isAbundant(i):
        abundants.append(i)

abundantSums = []

i = 0
while i < len(abundants):
    j = 0
    stop = False
    while j < len(abundants) and not stop:
        k = abundants[i] + abundants[j]
        if k > 28123:
            stop = True
        else:
            abundantSums.append(k)
            j += 1
    i += 1

uniqueSums = []
i = 0
for ele in abundantSums:
    i += 1
    if ele not in uniqueSums:
        uniqueSums.append(ele)

t = (28123*28124)//2
print(t - sum(uniqueSums))

print("...End")
