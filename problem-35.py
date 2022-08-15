# Problem 35

import math

print("Running...")

def isPrime(n):
    sqrtN = math.floor(math.sqrt(n))
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, sqrtN+1, 2):
        if n % i == 0:
            return False
    return True

primes = []
for i in range(100, 1000000):
    if isPrime(i):
        primes.append(i)

def arrToInt(arr):
    num = 0
    l = len(arr)
    for i in range(l):
        num += int(arr[i]) * 10**(l-i-1)
    return num

def isCircularPrime(p):
    s = str(p)
    l = len(s)
    arr = []
    for c in s:
        arr.append(c)
    snums = []
    for i in range(l):
        num = []
        j = i
        k = 0
        while k < l:
            if j == l:
                j = 0
            num.append(arr[j])
            j += 1
            k += 1
        snums.append(num)
    nums = []
    for s in snums:
        nums.append(arrToInt(s))
    stop = False
    i = 0
    while i < l and not stop:
        n = nums[i]
        if not isPrime(n):
            stop = True
        else:
            i += 1
    if i == l:
        return True
    else:
        return False

circularPrimes = []
for p in primes:
    if isCircularPrime(p):
        circularPrimes.append(p)
print(len(circularPrimes) + 13)

# There are 13 primes below 100 which are circular
# We are informed of this by the problem

print("...End")
