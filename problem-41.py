# Problem 41

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
for i in range(4, 10000000):
    if isPrime(i):
        primes.append(i)

def isPandigital(n):
    s = str(n)
    l = len(s)
    digs = []
    for i in range(1,l+1):
        digs.append(i)
    for c in s:
        intc = int(c)
        if intc not in digs:
            return False
        else:
            digs.remove(intc)
    return True

largestPanPrime = 2143
for p in primes:
    if isPandigital(p):
        largestPanPrime = p

# Trial and Error on Project Euler
# Up to 10,000,000 was enough
# Takes a min
print(largestPanPrime)

print("...End")
