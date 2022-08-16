# Problem 46

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
composites = []

for i in range(5, 10000, 2):
    if isPrime(i, primes):
        primes.append(i)
    else:
        composites.append(i)
#print(primes)

### Efficient Prime list generator
### Don't edit
doubleSquares = []
for i in range(1, 100):
    doubleSquares.append(2*i*i)

def canMakeComposite(c):
    i = 0
    a = primes[i]
    while a < c:
        j = 0
        b = doubleSquares[j]
        while b <= c - a:
            if a + b == c:
                return True
            else:
                j += 1
                b = doubleSquares[j]
        i += 1
        a = primes[i]
    return False

for c in composites:
    if not canMakeComposite(c):
        print(c)
        break

print("...End")
