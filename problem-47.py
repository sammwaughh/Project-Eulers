# Problem 47

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

for i in range(5, 200000, 2):
    if isPrime(i, primes):
        primes.append(i)

### Efficient Prime list generator
### Don't edit

# primes is all primes under 200,000

def findDistinctPrimeFactors(n):
    primeFactors = []
    i = 0
    pf = primes[i]
    while pf <= n:
        if n % pf == 0:
            primeFactors.append(pf)
        i += 1
        pf = primes[i]
    return primeFactors

distincts = []
found = False
i = 2
while not found:
    distincts.append(len(findDistinctPrimeFactors(i)))
    if sum(distincts[-4:]) == 16:
        print(i-3)
        print("FOUND")
        found = True
    i += 1

# Takes a minute

print("...End")
