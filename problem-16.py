# Problem 16

print("Running...")

twoToThousand = 2**1000

def sumDigits(n):
    s = str(n)
    sum = 0
    for c in s:
        sum += int(c)
    return sum

print(sumDigits(twoToThousand))

print("...End")
