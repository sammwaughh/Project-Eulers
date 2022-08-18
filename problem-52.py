# Problem 52

print("Running...")

def sameDigits(a, b):
    sa = str(a)
    sb = str(b)
    arr1 = []
    arr2 = []
    for c in sa:
        arr1.append(c)
    for c in sb:
        arr2.append(c)
    for ele in arr1:
        if ele not in arr2:
            return False
        else:
            arr2.remove(ele)
    if len(arr2) == 0:
        return True
    else:
        return False

i = 1
found = False
while not found:
    if sameDigits(3*i, 2*i):
        if sameDigits(4*i, 5*i):
            if sameDigits(2*i, 6*i):
                found = True
                print(i)
    i += 1

print("...End")