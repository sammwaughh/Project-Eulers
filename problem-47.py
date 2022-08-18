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

for i in range(5, 100000, 2):
    if isPrime(i, primes):
        primes.append(i)

### Efficient Prime list generator
### Don't edit

# primes is all primes under 100,000

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

i = 646
print(i, findDistinctPrimeFactors(i))

print("...End")
