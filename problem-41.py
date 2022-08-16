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
for i in range(4, 1000000):
    if isPrime(i):
        primes.append(i)
print(primes)

print("...End")
