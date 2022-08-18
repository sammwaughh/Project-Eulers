# Problem 50

import math

print("Running...")

### Efficient Prime list generator

def isPrime(n, knownPrimes):
    sqrtN = math.ceil(math.sqrt(n))
    i = 0
    tryp = 2
    while tryp < sqrtN:
        tryp = knownPrimes[i]
        if n % tryp == 0:
            return False
        i += 1
    return True

primes = [2,3]

for i in range(5, 1000000, 2):
    if isPrime(i, primes):
        primes.append(i)

### Efficient Prime list generator
### Don't edit
# primes is all primes under 1,000,000

bestL = 1
bestP = 1
last = primes[-1]
for i in range(len(primes)):
    j = 1
    arr = primes[i:i+j]
    s = sum(arr)
    l = len(arr)
    while s < last:
        if s in primes:
            if l > bestL:
                bestL = l
                bestP = s
        j += 1
        arr = primes[i:i+j]
        s = sum(arr)
        l = len(arr)

#Takes a minute or two

print(bestL, bestP)

print("...End")


