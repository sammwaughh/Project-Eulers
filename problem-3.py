# Problem 3
# Find the largest prime factor of 600851475143

print("Running...")

largestPrime = 0

num = 600851475143
def reduceNum(n):
    for i in range(2, n+1):
        if n % i == 0:
            return i, n//i

while num != 1:
    prime, num = reduceNum(num)
    if prime > largestPrime:
        largestPrime = prime

print(largestPrime)


print("...End")