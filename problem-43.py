# Problem 43

print("Running...")

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

tenDigitSet = [1,2,3,4,5,6,7,8,9,0]       
tenDigitPerms = producePerms(tenDigitSet)
print("Calculated Perms")

def arrToInt(arr):
    num = 0
    l = len(arr)
    for i in range(l):
        num += int(arr[i]) * 10**(l-i-1)
    return num

def hasProperty(arr):
    if arrToInt(arr[7:10]) % 17 == 0:
        if arrToInt(arr[6:9]) % 13 == 0:
            if arrToInt(arr[5:8]) % 11 == 0:
                if arrToInt(arr[4:7]) % 7 == 0:
                    if arrToInt(arr[3:6]) % 5 == 0:
                        if arrToInt(arr[2:5]) % 3 == 0:
                            if arrToInt(arr[1:4]) % 2 == 0:
                                return True
    return False

specials = []
for perm in tenDigitPerms:
    if hasProperty(perm):
        specials.append(arrToInt(perm))

print(specials)
print(sum(specials))

print("...End")
