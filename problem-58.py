# Problem 58

print("Running...")

### The Seive of Eratosthenes

### Efficient Prime list generator

from math import isqrt

def primes_less_than(n):
    if n <= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, isqrt(n)+1):
        if is_prime[i]:
            for x in range(i*i, n, i):
                is_prime[x] = False
    return is_prime

# True/False primes under 100,000
prime_bools = primes_less_than(100000)
prime_nums = [i for i in range(len(prime_bools)) if prime_bools[i]]




print("...End")