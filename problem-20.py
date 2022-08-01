# Problem 20

print("Running...")

def digitSum(n):
    s = str(n)
    sum = 0
    for c in s:
        sum += int(c)
    return sum

p = 1
for i in range(2, 101):
    p *= i

print(p)
print(digitSum(p))

print("...End")