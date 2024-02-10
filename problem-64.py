# Problem 64
from math import sqrt, floor

def isOddPeriod(n):
    pass

def countOddPeriods(n):
    count = 0
    for i in range(1, n+1):
        if floor(sqrt(i)) != sqrt(i):
            if isOddPeriod(i):
                count += 1
    return count


