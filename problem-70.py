# Problem 70

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def isRelPrime(a, b):
    if gcd(a, b) == 1:
        return True
    else:
        return False

def totient(n):
    count = 0
    for i in range(1, n):
        if isRelPrime(i, n):
            count += 1
    return count


print(totient(7000009))


