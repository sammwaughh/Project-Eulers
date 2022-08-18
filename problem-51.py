# Problem 51

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

for i in range(5, 1000000, 2):
    if isPrime(i, primes):
        primes.append(i)

### Efficient Prime list generator
### Don't edit
# primes is all primes under 1,000,000



print("...End")


