# Problem 92

print("Running...")

def nextInChain(n):
    s = str(n)
    sum = 0
    for c in s:
        sum += int(c)**2
    return sum

def is89(n):
    while n != 1 and n != 89:
        n = nextInChain(n)
    if n == 1:
        return False
    else:
        return True

count = 0
for i in range(1, 100001):
    if is89(i):
        count += 1
print(count)

print("...End")