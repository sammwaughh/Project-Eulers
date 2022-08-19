# Problem 751

import math

print("Running...")

def nextTerm(b):
    f = math.floor(b)
    return f * (b - f + 1)

theta = 2.956938891377988

b = theta
aString = ""
i = 0
while len(aString) < 25:
    a = math.floor(b)
    aString += str(a)
    b = nextTerm(b)
    i += 1
print(aString[1:25])

if aString[1:25] == theta[2:26]:
    print(theta)

print("...End")