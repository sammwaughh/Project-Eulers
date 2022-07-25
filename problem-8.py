# Problem 8

print("Running...")

numFile = open("8.txt", "r")
num = numFile.read()
num = num.replace("\n", "")

maxp = 1

for i in range(987):
    s = num[i:i+13]
    p = 1
    for c in s:
        p *= int(c)
    if p > maxp:
        maxp = p

print(maxp)

print("...End")
