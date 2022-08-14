# Problem 22

print("Running...")

file22 = open("22.txt", "r")
f = file22.read()
file22.close()
f = f[1:-1]
nameList = f.split("\",\"")
alphaNameList = sorted(nameList)


def nameScore(name):
    score = 0
    for c in name:
        score += ord(c) - 64
    return score

total = 0
for i in range(1, 5164):
    total += i * nameScore(alphaNameList[i-1])
print(total)

print("...End")
