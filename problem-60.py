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

prime_bools = primes_less_than(1000)
prime_nums = [i for i in range(len(prime_bools)) if prime_bools[i]]
is_prime = primes_less_than(1000000)

l = len(prime_nums)

print("Done calculating primes")

def evaluate_set(set):
    for i in range(len(set)):
        for j in range(i+1, len(set)):
            p1 = int(str(set[i]) + str(set[j]))
            p2 = int(str(set[j]) + str(set[i]))
            if not is_prime[p1]:
                return False
            if not is_prime[p2]:
                return False
    return True

def sort_list_of_tuples(lst):
    sorted_list = sorted(lst, key=lambda x: x[1])
    return sorted_list

prime_sets = []
for i in range(l):
    for j in range(i+1, l):
        print(i, j)
        for k in range(j+1, l):
            for m in range(k+1, l):
                for v in range(m+1, l):
                    set = [prime_nums[i],
                            prime_nums[j],
                            prime_nums[k],
                            prime_nums[m],
                            prime_nums[v]]
                    prime_sets.append((set, sum(set)))
print("End of prime set construction")

sorted_sets = sort_list_of_tuples(prime_sets)
for set in sorted_sets:
    if evaluate_set(set[0]):
        print(set)
        break

print("...End")