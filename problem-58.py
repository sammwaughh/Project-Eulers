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

# True/False primes under 1,000,000,000
prime_bools = primes_less_than(1000000000)
prime_nums = [i for i in range(len(prime_bools)) if prime_bools[i]]

print("Done calculating primes")

def calc_north_east(n):
    return 4*n*n - 10*n + 7

def calc_north_west(n):
    return 4*n*n - 8*n + 5

def calc_south_west(n):
    return 4*n*n - 6*n + 3

side_length = 1
stop = False
p = 0
while not stop:
    side_length += 2
    n = (side_length + 1) // 2
    if prime_bools[calc_north_east(n)]:
        p += 1
    if prime_bools[calc_north_west(n)]:
        p += 1
    if prime_bools[calc_south_west(n)]:
        p += 1

    l = side_length*2 - 1
    ratio = p / l
    if ratio < 0.1:
        stop = True
        
print(side_length)
    
print("...End")