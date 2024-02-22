# Problem 72

import time
start_time = time.time()

def coPrimeLessThan(n, prime_factors):
    seive = [None]
    for i in range(1, n):
        seive.append(i)
    for p in prime_factors:
        index = p
        while index < n:
            seive[index] = None
            index += p
    coprimes = []
    for ele in seive:
        if ele != None:
            coprimes.append(ele)
    return coprimes

def otherCoPrimeFunction(n, prime_factors):
    pass

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

def primeFactors(n):
    factors = []
    index = 0
    prime = knownPrimes[index]
    while n != 1:
        if n % prime == 0:
            factors.append(prime)
            while n % prime == 0:
                n = n // prime
        index += 1
        prime = knownPrimes[index]
    return factors

limit = 75000
knownPrimes = generatePrimeUpTo(limit+100)

biglist = [None, None]
for i in range(2, limit):
    biglist.append(primeFactors(i))


print(biglist[-1])


# total = 0
# for i in range(1, 9):
#     i_prime_factors = primeFactors(i)
#     total += len(coPrimeLessThan(i, i_prime_factors))
# print(total)


end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", round(execution_time, 2), "seconds")


