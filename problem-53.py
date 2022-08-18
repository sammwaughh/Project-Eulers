# Problem 53

import math

print("Running...")

factorials = []
for i in range(101):
    factorials.append(math.factorial(i))

def nChooseR(n, r):
    return (factorials[n])//(factorials[r]*factorials[n-r])

count = 0
for n in range(1, 101):
    r = 1
    while r <= n:
        if nChooseR(n, r) > 1000000:
            count += 1
        r += 1
print(count)


print("...End")