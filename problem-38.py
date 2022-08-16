# Problem 38

print("Running...")

def makeNum(i, n):
    s = ""
    for j in range(1, n+1):
        s += str(i*j)
    return int(s)

def isPandigital(n):
    s = str(n)
    if len(s) != 9:
        return False
    digs = [1,2,3,4,5,6,7,8,9]
    for c in s:
        intc = int(c)
        if intc not in digs:
            return False
        else:
            digs.remove(intc)
    return True



print("...End")
