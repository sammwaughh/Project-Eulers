# Problem 24
import math

print("Running...")

# A more general implementation
decdigits = [0,1,2,3,4,5,6,7,8,9]

def findNthPermutation(digits, n):
    if len(digits)==0:
        return []
    else:
        l = len(digits)
        f = math.factorial(l-1)
        i = 0
        while n > f:
            n -= f
            i += 1
        start = digits[i]
        digits.remove(start)
        return [start] + findNthPermutation(digits, n)

print(findNthPermutation(decdigits, 1000000))

print("...End")
