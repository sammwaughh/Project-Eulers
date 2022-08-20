# Problem 54

print("Running...")

file54 = open("54.txt", "r")
arr = file54.read().split("\n")
arr2 = []
for ele in arr:
    arr2.append(ele.split(" "))
hands = arr2[:-1]
print(hands)

print("...End")