# Problem 56

print("Running...")

def digitSum(n):
    s = str(n)
    sum = 0
    for c in s:
        sum += int(c)
    return sum

bestSum = 0
for a in range(1, 101):
    for b in range(1, 101):
        p = a**b
        d = digitSum(p)
        if d > bestSum:
            bestSum = d
print(bestSum)

print("...End")