# Problem 72

import time
from copy import copy

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def coPrimeLessThan(n):
    count = 0
    for i in range(1, n):
        if gcd(i, n) == 1:
            count += 1
    return count

def generatePrimeUpTo(n):
    seive = [None, None, ]
    for i in range(2, n):
        seive.append(i)
    i = 2
    while i < n:
        prime = seive[i]
        index = prime
        if prime != None:
            index += prime
            while index < n:
                seive[index] = None
                index += prime
        i += 1
    primes = []
    for ele in seive:
        if ele != None:
            primes.append(ele)
    return primes


def findPrimeFactors(n):
    primes = []
    pass


def newCoPrimeLessThan(n):
    # prime-factors = findPrimeFactors(n)
    pass


def numberOfFractions(d):
    total = 0
    for i in range(1, d+1):
        total += coPrimeLessThan(i)
    return total


start_time = time.time()
print(generatePrimeSeive(1000000))
# print(numberOfFractions(20000))
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", round(execution_time, 2), "seconds")


