# Problem 2

print("Running...")

sum = 0
a = 1
b = 2

while b < 4000000:
    if b % 2 == 0:
        sum += b
    t = a + b
    a = b
    b = t

print(sum)

print("...End")