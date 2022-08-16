# Problem 37

import math

print("Running...")

def isPrime(n):
    sqrtN = math.floor(math.sqrt(n))
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, sqrtN+1, 2):
        if n % i == 0:
            return False
    return True

primes = [2,3]
for i in range(4, 1000000):
    if isPrime(i):
        primes.append(i)
#print(primes)
truncPrimes = []

for p in primes[6:]:
    trunc = True
    l = len(str(p))
    i = 1
    while i < l and trunc:
        if int(str(p)[i:]) not in primes:
            trunc = False
        else:
            i += 1
    j = -1
    negl = l * -1
    while j > negl and trunc:
        if int(str(p)[:j]) not in primes:
            trunc = False
        else:
            j -= 1
    if trunc:
        truncPrimes.append(p)

print(sum(truncPrimes))

print("...End")
