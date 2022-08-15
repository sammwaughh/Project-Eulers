# Problem 32

print("Running...")

# Generate a list of lists. Each element is a list of the digits 1-9
# which represents a unique permuation of those digits

def producePerms(set):
    if len(set) == 1:
        return [set]
    else:
        perms = []
        for i in range(len(set)):
            setdash = set.copy()
            ele = set[i]
            first = [ele]
            setdash.remove(ele)
            smallerPerms = producePerms(setdash)
            for smallerSet in smallerPerms:
                perms.append(first + smallerSet)
        return perms

nineDigitSet = [1,2,3,4,5,6,7,8,9]       
nineDigitPerms = producePerms(nineDigitSet)

def arrToInt(arr):
    num = 0
    l = len(arr)
    for i in range(l):
        num += arr[i] * 10**(l-i-1)
    return num

prods = []

for perm in nineDigitPerms:
    p1 = arrToInt(perm[5:9])
    m1 = arrToInt(perm[:4])
    m2 = perm[4]
    m3 = arrToInt(perm[:2])
    m4 = arrToInt(perm[2:5])
    if m1*m2 == p1 or m3*m4 == p1:
        if p1 not in prods:
            prods.append(p1)

print(prods)
print(sum(prods))

print("...End")
