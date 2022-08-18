# Problem 49

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

for i in range(5, 10000, 2):
    if isPrime(i, primes):
        primes.append(i)

### Efficient Prime list generator
### Don't edit
# primes is all primes under 10,000

def isBiPermute(p, q):
    sp = str(p)
    sq = str(q)
    arr1 = []
    arr2 = []
    for c in sp:
        arr1.append(c)
    for c in sq:
        arr2.append(c)
    for digit in arr1:
        if digit in arr2:
            arr2.remove(digit)
        else:
            return False
    return True

def isPermute(x, y, z):
    if isBiPermute(x, y) and isBiPermute(x, z):
        return True
    else:
        return False

for i in range(1000, 10000):
    if i in primes:
        bound = (10000-i)//2
        for j in range(1, bound):
            b = i+j
            if b in primes:
                c = b+j
                if c in primes:
                    if isPermute(i,b,c):
                        print((i, b, c))

print("...End")


