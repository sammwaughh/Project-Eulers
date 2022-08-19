# Problem 92

print("Running...")

squares = [i**2 for i in range(10)]

def nextInChain(n):
    s = str(n)
    sum = 0
    for c in s:
        sum += squares[int(c)]
    return sum

def is89(n):
    while n != 1 and n != 89:
        n = nextInChain(n)
    if n == 89:
        return True
    else:
        return False

count = 0
for i in range(1, 10000000):
    if is89(i):
        count += 1
print(count)

print("...End")