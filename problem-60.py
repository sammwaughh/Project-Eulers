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

prime_bools = primes_less_than(10000)
prime_nums = [i for i in range(len(prime_bools)) if prime_bools[i]]
is_prime = primes_less_than(100000000)

print("Calculated primes.")

def evaluate_pair(pair):
    q1 = pair[0]
    q2 = pair[1]
    p1 = int(str(q1) + str(q2))
    p2 = int(str(q2) + str(q1))
    if is_prime[p1] and is_prime[p2]:
        return True

good_pairs = []
for i in range(len(prime_nums)):
    for j in range(i+1, len(prime_nums)):
        pair = [prime_nums[i], prime_nums[j]]
        if evaluate_pair(pair):
            good_pairs.append(pair)

good_trips = []
for pair in good_pairs:
    start = pair[1]
    for x in prime_nums:
        if x > start:
            if evaluate_pair([pair[0], x]) and evaluate_pair([pair[1], x]):
                good_trips.append([pair[0], pair[1], x])

good_quads = []
for trip in good_trips:
    start = trip[2]
    for x in prime_nums:
        if x > start:
            if evaluate_pair([trip[0], x]) and evaluate_pair([trip[1], x]) and evaluate_pair([trip[2], x]):
                good_quads.append([trip[0], trip[1], trip[2], x])

good_quints = []
for quad in good_quads:
    start = quad[3]
    for x in prime_nums:
        if x > start:
            if evaluate_pair([quad[0], x]) and evaluate_pair([quad[1], x]) and evaluate_pair([quad[2], x]) and evaluate_pair([quad[3], x]):
                good_quints.append([quad[0], quad[1], quad[2], quad[3], x])

print(good_quints)
print(sum(good_quints))

print("...End")