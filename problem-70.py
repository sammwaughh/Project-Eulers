# Problem 70

import time
start_time = time.time()

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

def euler_totient(n):
    result = n  # Initialize result as n
    index = 0
    p = knownPrimes[index]
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        index += 1
        p = knownPrimes[index]
    if n > 1:
        result -= result // n
    return result

limit = 1000000
knownPrimes = generatePrimeUpTo(limit+100)


end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", round(execution_time, 2), "seconds")


