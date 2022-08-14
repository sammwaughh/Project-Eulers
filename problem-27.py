# Problem 27

import math

print("Running...")

def isPrime(n):
    sqrtN = math.floor(math.sqrt(n))
    if n == 2:
        return True
    if n % 2 == 0 or n==1 or n==0:
        return False
    for i in range(3, sqrtN+1, 2):
        if n % i == 0:
            return False
    return True



print("...End")
