# Problem 33

print("Running.. .")

def isSpecial(n, d):
    val = n/d
    n1 = n // 10
    n2 = n - n1*10
    d1 = d // 10
    d2 = d - d1*10
    if n2 == 0 or d2 == 0:
        return False
    if n1 == d1:
        if n2/d2 == val:
            return True
    if n1 == d2:
        if n2/d1 == val:
            return True
    if n2 == d1:
        if n1/d2 == val:
            return True
    if n2 == d2:
        if n1/d1 == val:
            return True
    return False

specials = []
for i in range(10, 100):
    for j in range(i+1, 100):
        if isSpecial(i, j):
            specials.append((i,j))

print(specials)
# Prints [(16, 64), (19, 95), (26, 65), (49, 98)]
# [1/4, 1/5, 2/5, 1/2]
# => Product is 1/100 => Ans == 100

print("...End")
