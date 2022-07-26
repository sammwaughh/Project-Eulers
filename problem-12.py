# Problem 12
import math

print("Running...")

def numFactors(n):
    sqrtn = math.sqrt(n)
    upperBound = math.floor(sqrtn)
    count = 2
    for i in range(2, upperBound+1):
        if n % i == 0:
            count += 2
    if sqrtn == upperBound:
        count -= 1
    return count

found = False
t = 0
i = 1
while not found:
    t += i
    i += 1
    if numFactors(t) > 500:
        found = True

print(t)

print("...End")
