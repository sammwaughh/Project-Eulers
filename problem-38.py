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

panMults = []
i = 1
# i cannot exceed 10,000 because 
# a number longer than nine digits will be made for n >= 2
while i < 10000:
    n = 2
    stop = False
    while not stop:
        res = makeNum(i, n)
        if len(str(res)) > 9:
            stop = True
        elif isPandigital(res):
            panMults.append(res)
        n += 1
    i += 1

print(max(panMults))

print("...End")
