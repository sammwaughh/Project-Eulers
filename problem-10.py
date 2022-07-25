# Problem 10
# Find the sum of all the primes below two million.
import math

print("Running...")

def isPrime(foundPrimes, n):
    m = math.floor(math.sqrt(n))
    i = 0
    p = foundPrimes[i]
    l = len(foundPrimes)
    while p <= m and i < l:
        if n % p == 0:
            return False
        i += 1
        p = foundPrimes[i]
    return True

primes = [2,3]

counter = 4
while primes[-1] < 2000000:
    if isPrime(primes, counter):
        primes.append(counter)
    counter += 1

print(sum(primes[:-1]))

print("...End")
