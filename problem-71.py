# Problem 71

from math import floor

print("Running...")

def isProper(n, d):
    while n != 0:
        rem = d % n
        d = n
        n = rem
    if d == 1:
        return True
    else:
        return False

def fractionsCloseToTarget(d):
    middle = d * 3/7
    numerator = floor(middle)
    while not isProper(numerator, d):
        numerator -= 1
        if numerator <= 0:
            return 0, 0, 0
    return numerator/d, numerator, d

fractionDict = {}
arr = []
for i in range(1,1000000):
    decimal, n, d = fractionsCloseToTarget(i)
    arr.append(decimal)
    fractionDict[decimal] = (n, d)

arr.sort()

#print(arr[-3:])
#print(fractionDict[arr[-1]])
print(fractionDict[arr[-2]][0])

print("...End")