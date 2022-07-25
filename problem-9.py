# Problem 9
# There exists exactly one Pythagorean triplet for which 
# a + b + c = 1000.
# Find the product abc.
import math

print("Running...")

for a in range(333):
    for b in range(a, a + (1000-a)//2):
        csquared = a**2 + b**2
        c = math.sqrt(csquared)
        if math.floor(c) == c:
            if a + b + c == 1000:
                print(a, b, c)
                print(a*b*c)

print("...End")
