# Problem 61

print("Running...")

def triangles_under_m(m):
    i = 1
    is_triangle = [False] * m
    t = 1
    while t < m:
        is_triangle[t] = True
        i += 1
        t += i
    return is_triangle

def squares_under_m(m):
    i = 1
    is_square = [False] * m
    t = 1
    while t < m:
        is_square[t] = True
        i += 2
        t += i
    return is_square

def pentagonals_under_m(m):
    i = 1
    is_pentagonal = [False] * m
    t = 1
    while t < m:
        is_pentagonal[t] = True
        i += 3
        t += i
    return is_pentagonal

def hexagonals_under_m(m):
    i = 1
    is_hexagonal = [False] * m
    t = 1
    while t < m:
        is_hexagonal[t] = True
        i += 4
        t += i
    return is_hexagonal

def heptagonals_under_m(m):
    i = 1
    is_heptagonal = [False] * m
    t = 1
    while t < m:
        is_heptagonal[t] = True
        i += 5
        t += i
    return is_heptagonal

def octagonals_under_m(m):
    i = 1
    is_octagonal = [False] * m
    t = 1
    while t < m:
        is_octagonal[t] = True
        i += 6
        t += i
    return is_octagonal


triangles = triangles_under_m(10000)
squares = squares_under_m(1000)
pentagonals = pentagonals_under_m(1000)
hexagonals = hexagonals_under_m(1000)
heptagonals = heptagonals_under_m(1000)
octagonals = octagonals_under_m(1000)

print("...End")