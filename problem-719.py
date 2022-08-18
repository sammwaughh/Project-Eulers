# Problem 719

import math

print("Running...")

# Make all binary numbers up to length n
# Example: n=3 => 000,001,...,110,111
def makeBins(n):
    bins = []
    bound = 2**n
    for i in range(bound):
        bins.append(str(bin(i))[2:].zfill(n))
    return bins

bins = [0]
for i in range(1, 13):
    bins.append(makeBins(i))

squares = []
for i in range(4, 1000001):
    squares.append(i**2)

def parseSum(s):
    arr = s.split('+')
    sum = 0
    for n in arr:
        sum += int(n)
    return sum

def splitSum(square, root):
    s = str(square)
    arr = []
    for c in s:
        arr.append(c)
    # arr = ['6', '7', '2', '4']
    l0 = len(arr) - 1
    combos = bins[l0]
    i = 0
    l = 2**l0
    while i < l:
        combo = combos[i]
        expression = arr[0]
        for j in range(l0):
            if combo[j] == '1':
                expression += '+'
            expression += arr[j+1]
        if parseSum(expression) == root:
            return True
        i += 1
    return False

snumbers = []
i = 0
for square in squares:
    if i % 100 == 0:
        print(i)
    root = math.sqrt(square)
    if splitSum(square, root):
        snumbers.append(square)
    i += 1

#print(snumbers)
print(sum(snumbers))

print("...End")