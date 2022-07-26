# Problem 11

print("Running...")

gridFile = open("11.txt", "r")
grid = []
for line in gridFile:
    strArr = line.strip().split(" ")
    arr = []
    for s in strArr:
        arr.append(int(s))
    grid.append(arr)

greatestProduct = 0

for i in range(20):
    for j in range(17):
        p = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
        if p > greatestProduct:
            greatestProduct = p


for i in range(17):
    for j in range(20):
        p = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
        if p > greatestProduct:
            greatestProduct = p

for i in range(17):
    for j in range(17):
        p = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
        if p > greatestProduct:
            greatestProduct = p

for i in range(19, 2, -1):
    for j in range(19, 2, -1):
        p = grid[i][j] * grid[i-1][j-1] * grid[i-2][j-2] * grid[i-3][j-3]
        if p > greatestProduct:
            greatestProduct = p

print(greatestProduct)

print("...End")
