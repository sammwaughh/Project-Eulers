# Problem 64
from math import sqrt, floor

"""def period(n):
    root = sqrt(n)
    floor_root = floor(sqrt(n))
    if floor_root == root:
        return [False, False]
    n = 1 / (root - floor_root)
    period_arr = [int(n)]
    i = 0
    while i < 10:
        if round(n-floor_root, 4) == round(root, 4):
            break
        n = 1 / (n - int(n))
        period_arr.append(int(n))
        i += 1
    return period_arr"""

def rationaliseReciprocal(numerator, surd, integer):
    denominator = surd - integer**2
    numerator = (surd, integer*-1)
    return numerator, denominator

print(rationaliseReciprocal(23, -4))

def getIntegerPart(numerator, denominator):
    integerPart = int((sqrt(numerator[0]) + numerator[1])/denominator)
    return integerPart

def subtractInteger(fraction, integerPart):
    pass

def period(n):
    # Example n = 23
    root = sqrt(n) # root = 4.795
    adder = floor(root) # adder = 4
    pass


# for i in range(14):
#     print(i, period(i))

def countOddPeriods(n):
    count = 0
    for i in range(2, n+1):
        p = period(i)
        l = len(p)
        if l % 2 != 0:
            count += 1
        print(i, p, l)
    return count

# print(countOddPeriods(100))
