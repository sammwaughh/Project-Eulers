a = 1
b = 2
counter = 0
ourSum = 0

while b < 4000000:
    if counter % 3 == 0:
        ourSum += b
    t = a + b
    a = b
    b = t
    counter += 1

print(ourSum)