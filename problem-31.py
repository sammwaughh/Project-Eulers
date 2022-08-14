# Problem 31

print("Running...")

def compareSets(A, B):
    pass

def distinctSet(S):
    pass

def addingCombos(target, set):
    print(target, set)
    combos = []
    for ele in set:
        if ele == target:
            combos.append([ele])
        elif ele < target:
            for ele2 in addingCombos(target - ele, set):
                combos.append([ele] + ele2)
    return combos

print(addingCombos(4, [1,2]))

print("...End")
