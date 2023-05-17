# Problem 66

from math import floor, sqrt

print("Running...")

def solveEquationY(x, D):
    ySquared = (x**2 - 1) / D
    a = sqrt(ySquared)
    b = floor(sqrt(ySquared))
    if a == b:
        return True, b
    else:
        return False, -1

def solveEquation(D):
    # Solve x^2 - Dy^2 = 1
    x = 1
    solved = False
    while not solved:
        x += 1
        solved, y = solveEquationY(x, D) 
    return x, y

d = 2
largestX = -1
bestD = None
while d <= 1000:
    print(d)
    if sqrt(d) != floor(sqrt(d)):
        x, y = solveEquation(d)
        if x > largestX:
            largestX = x
            bestD = d
    d += 1

print(largestX, bestD)

print("...End")
