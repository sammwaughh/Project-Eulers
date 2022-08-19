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





print("...End")