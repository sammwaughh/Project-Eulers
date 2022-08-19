# Problem 684

print("Running...")

def digitSum(n):
    s = str(n)
    sum = 0
    for c in s:
        sum += int(c)
    return sum

def s(n):
    Found = False
    i = 0
    while not Found:
        d = digitSum(i)
        if d == n:
            Found = True
        else:
            i += 1
    return i

def S(k):
    sum = 0
    for n in range(1, k+1):
        sum += s(n)
    return sum

sum = 0
a = 0
b = 1
i = 1
while i < 90:
    t = a + b
    a = b
    b = t
    # sum += S(b)
    i += 1
print(S(2880067194370816120))

print("...End")