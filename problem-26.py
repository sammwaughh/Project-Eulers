# Problem 26

from math import remainder
from socket import NI_NUMERICHOST


print("Running...")

def lengthOfRepeat(n):
    count = 1
    remainders = [1]
    stop = False
    while not stop:
        numerator = remainders[-1]
        while numerator < n:
            numerator *= 10
        remainder = numerator % n
        if remainder == 0:
            stop = True
        if remainder in remainders:
            stop = True
        else:
            remainders.append(remainder)
            count += 1
    return count

bestD = 1
longestCycle = 1

for i in range(1, 1000):
    cycleLen = lengthOfRepeat(i)
    if cycleLen > longestCycle:
        bestD = i
        longestCycle = cycleLen

print(bestD)

print("...End")
