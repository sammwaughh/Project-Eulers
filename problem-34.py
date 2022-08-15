# Problem 34

import math

print("Running...")

# Guessed there were no more after 10,000,000
# Assumption was correct. Answer is 145 + 40585 == 40730

def digitFactorial(n):
    s = str(n)
    sum = 0
    for c in s:
        sum += math.factorial(int(c))
    return sum

sum = 0
for i in range(10, 10000000):
    if i == digitFactorial(i):
        sum += i

print(sum)

print("...End")
