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
squares = squares_under_m(10000)
pentagonals = pentagonals_under_m(10000)
hexagonals = hexagonals_under_m(10000)
heptagonals = heptagonals_under_m(10000)
octagonals = octagonals_under_m(10000)

def list_in_range(arr):
    # Starting list
    new_arr = []
    for i in range(1000,10000):
        if arr[i]:
            new_arr.append(i)
    return new_arr

triangles = list_in_range(triangles)
squares = list_in_range(squares)
pentagonals = list_in_range(pentagonals)
hexagonals = list_in_range(hexagonals)
heptagonals = list_in_range(heptagonals)
octagonals = list_in_range(octagonals)

def triangles_begin_with_x(x):
    # e.g. x = 81 so number could be 8100 or 8128
    i = 100 * x
    arr = []
    end = i + 100
    while i < end:
        if triangles[i]:
            arr.append(i)
        i += 1
    return arr

def squares_begin_with_x(x):
    # e.g. x = 81 so number could be 8100 or 8128
    i = 100 * x
    arr = []
    end = i + 100
    while i < end:
        if squares[i]:
            arr.append(i)
        i += 1
    return arr

def pentagonals_begin_with_x(x):
    # e.g. x = 81 so number could be 8100 or 8128
    i = 100 * x
    arr = []
    end = i + 100
    while i < end:
        if pentagonals[i]:
            arr.append(i)
        i += 1
    return arr

def hexagonals_begin_with_x(x):
    # e.g. x = 81 so number could be 8100 or 8128
    i = 100 * x
    arr = []
    end = i + 100
    while i < end:
        if hexagonals[i]:
            arr.append(i)
        i += 1
    return arr

def heptagonals_begin_with_x(x):
    # e.g. x = 81 so number could be 8100 or 8128
    i = 100 * x
    arr = []
    end = i + 100
    while i < end:
        if heptagonals[i]:
            arr.append(i)
        i += 1
    return arr

def octagonals_begin_with_x(x):
    # e.g. x = 81 so number could be 8100 or 8128
    i = 100 * x
    arr = []
    end = i + 100
    while i < end:
        if octagonals[i]:
            arr.append(i)
        i += 1
    return arr

# Main program

def next_polygons(x, polygons_found, arr):
    c = 0
    for i in range(6):
        if polygons_found[i]:
            c += 1
    if c == 6:
        print(arr)
        return True

    # Cycle begins
    startx = int(str(x)[-2:])

    if not polygons_found[0]:
        p3 = triangles_begin_with_x(startx)
        polygons_found[0] = True
        if p3:
            for p in p3:
                startp = int(str(p)[-2:])
                if startp >= 10:
                    new_arr = arr + [p]
                    return next_polygons(startp, polygons_found, new_arr)
        else:
            return False
    
    if not polygons_found[1]:
        p4 = squares_begin_with_x(startx)
        polygons_found[1] = True
        if p4:
            for p in p4:
                startp = int(str(p)[-2:])
                if startp >= 10:
                    new_arr = arr + [p]
                    return next_polygons(startp, polygons_found, new_arr)
        else:
            return False

    if not polygons_found[2]:
        p5 = pentagonals_begin_with_x(startx)
        polygons_found[2] = True
        if p5:
            for p in p5:
                startp = int(str(p)[-2:])
                if startp >= 10:
                    new_arr = arr + [p]
                    return next_polygons(startp, polygons_found, new_arr)
        else:
            return False

    if not polygons_found[3]:
        p6 = hexagonals_begin_with_x(startx)
        polygons_found[3] = True
        if p6:
            for p in p6:
                startp = int(str(p)[-2:])
                if startp >= 10:
                    new_arr = arr + [p]
                    return next_polygons(startp, polygons_found, new_arr)
        else:
            return False

    if not polygons_found[4]:
        p7 = heptagonals_begin_with_x(startx)
        polygons_found[4] = True
        if p7:
            for p in p7:
                startp = int(str(p)[-2:])
                if startp >= 10:
                    new_arr = arr + [p]
                    return next_polygons(startp, polygons_found, new_arr)
        else:
            return False
    

# Start number
i = 0
l = len(octagonals)
while i < l:
    y = octagonals[i]
    arr = [y]
    polygons_found = [False, False, False, False, False, True]
    print(i)

    good = next_polygons(y, polygons_found, arr)
    if good:
        break
    i += 1


print("...End")