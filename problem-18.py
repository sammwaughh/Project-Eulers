# Problem 18
# Maximum path sum I

print("Running...")

# Setting up the array
file18 = open("18.txt", "r")
filem = file18.readlines()
m = []
for row in filem:
    mrow = []
    r = row.strip().split(" ")
    for ele in r:
        mrow.append(int(ele))
    m.append(mrow)

# Iterative
def improveBase(topRow, bottomRow):
    newTop = []
    for i in range(len(topRow)):
        current = topRow[i]
        a = bottomRow[i]
        b = bottomRow[i+1]
        if a > b:
            newTop.append(current + a)
        else:
            newTop.append(current + b)
    return newTop

while len(m) > 1:
    penultimateRow = m[-2]
    lastRow = m[-1]
    #print(penultimateRow, lastRow)
    newBase = improveBase(penultimateRow, lastRow)
    #print(newBase)
    m = m[:-2]
    m.append(newBase)
print(m[0][0])




file18.close()
print("...End")
