# Problem 23
import math

print("Running...")

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

abundants = []
for i in range(2, 28123):
    if divisorSum(i) > i:
        abundants.append(i)

#print(abundants)
#print(len(abundants))
crossAbundants = []
for x in abundants:
    for y in abundants:
        crossAbundants.append(x+y)

print(len(crossAbundants))
bigSum = (28123*28124)//2
i = 0
complementSum = 0
betterCrossAbundants = []
for ele in crossAbundants:
    if ele < 28124 and ele not in betterCrossAbundants:
        betterCrossAbundants.append(ele)

print(len(betterCrossAbundants))



print("...End")