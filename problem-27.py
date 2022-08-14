# Problem 27

import math

print("Running...")

def isPrime(n):
    if n <= 1 or n%2 == 0:
        return False
    sqrtN = math.floor(math.sqrt(n))
    if n == 2:
        return True
    for i in range(3, sqrtN+1, 2):
        if n % i == 0:
            return False
    return True

def computeQuadratic(n, a, b):
    val = n**2 + n*a + b
    return val

bestCount = 0
bestPair = None

for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        n = 0
        stop = False
        while not stop:
            if isPrime(computeQuadratic(n, a, b)):
                n += 1
            else:
                stop = True
        if n > bestCount:
            bestCount = n
            bestPair = (a, b, n)

print(bestPair)
print(bestPair[0]*bestPair[1])

print("...End")
