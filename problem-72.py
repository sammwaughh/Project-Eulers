# Problem 72

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

primeList = generatePrimeUpTo(1000000)







# print(numberOfFractions(20000))
end_time = time.time()
execution_time = end_time - start_time
print("Execution time:", round(execution_time, 2), "seconds")


