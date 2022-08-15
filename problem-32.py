# Problem 32

print("Running...")

# Generate a list of lists. Each element is a list of the digits 1-9
# which represents a unique permuation of those digits
permutations = []

digits = [1,2,3,4]
bins = []
for i in range(2**9):
    bins.append(str(bin(i))[2:].zfill(9))

startSet = [1,2,3,4]

def producePerms(set):
    if set == None or len(set) == 0:
        return []
    else:
        perms = []
        for ele in set:
            setdash = set.remove(ele)
            first = [ele]
            for smallerSet in producePerms(setdash):
                perms.append(first + smallerSet)
        return perms
        
print(producePerms(startSet))
            

print("...End")
