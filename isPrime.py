# Check if a number is a prime number
import math

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

print(isPrime(47000001))

