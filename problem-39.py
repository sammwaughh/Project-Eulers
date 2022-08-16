# Problem 39

print("Running...")

def isRightTriangle(tup):
    if tup[0]**2 + tup[1]**2 == tup[2]**2:
        return True
    else:
        return False

def generateTriangles(p):
    triangles = []
    m = p//2
    # a in the length of the base
    for a in range(1, m+1):
        # rem is the length left for the other two sides
        rem = p - a
        # b is the length of the second side
        for b in range(1, rem):
            # c is the length of the third side
            c = rem - b
            triangles.append((a,b,c))
    return triangles

def right(triangles):
    ts = []
    for t in triangles:
        if isRightTriangle(t):
            ts.append(t)
    return ts

mostTs = 0
bestI = 0
for i in range(10, 1001):
    s = len(right(generateTriangles(i)))
    if s > mostTs:
        mostTs = s
        bestI = i
# Takes about 2 mins
print(bestI)

print("...End")
