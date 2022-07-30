largestPrime = 0

def reduceNum(n):
    for i in range(2, n+1):
        if n % i == 0:
            return i, n//i

ourNumber = 600851475143
while ourNumber != 1:
    prime, ourNumber = reduceNum(ourNumber)
    if prime > largestPrime:
        largestPrime = prime

print(largestPrime)
