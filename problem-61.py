# Problem 61

import copy

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

def next_polygons(startx, polygons_found, arr, record):
    c = 0
    for i in range(6):
        if polygons_found[i]:
            c += 1
    if c == 6 and len(arr) == 6:
        end = arr[-1]
        start = arr[0]
        if str(end)[-2:] == str(start)[:2]:
            print(arr)
            print(record)
            print(sum(arr))
    new_polygons_found = copy.copy(polygons_found)
    new_arr = copy.copy(arr)
    new_record = copy.copy(record)

    if not polygons_found[0]:
        p3 = triangles_begin_with_x(startx)
        if p3:
            for p in p3:
                startp = int(str(p)[-2:])
                if startp >= 10:
                    new_polygons_found[0] = True
                    new_arr = arr + [p]
                    new_record = record + ["tri"]
                    next_polygons(startp, new_polygons_found, new_arr, new_record)
    new_polygons_found = copy.copy(polygons_found)
    new_arr = copy.copy(arr)
    new_record = copy.copy(record)

    if not polygons_found[1]:
        p4 = squares_begin_with_x(startx)
        if p4:
            for p in p4:
                startp = int(str(p)[-2:])
                if startp >= 10:
                    new_polygons_found[1] = True
                    new_arr = arr + [p]
                    new_record = record + ["square"]
                    next_polygons(startp, new_polygons_found, new_arr, new_record)
    new_polygons_found = copy.copy(polygons_found)
    new_arr = copy.copy(arr)
    new_record = copy.copy(record)

    if not polygons_found[2]:
        p5 = pentagonals_begin_with_x(startx)
        if p5:
            for p in p5:
                startp = int(str(p)[-2:])
                if startp >= 10:
                    new_polygons_found[2] = True
                    new_arr = arr + [p]
                    new_record = record + ["pent"]
                    next_polygons(startp, new_polygons_found, new_arr, new_record)
    new_polygons_found = copy.copy(polygons_found)
    new_arr = copy.copy(arr)
    new_record = copy.copy(record)

    if not polygons_found[3]:
        p6 = hexagonals_begin_with_x(startx)
        if p6:
            for p in p6:
                startp = int(str(p)[-2:])
                if startp >= 10:
                    new_polygons_found[3] = True
                    new_arr = arr + [p]
                    new_record = record + ["hex"]
                    next_polygons(startp, new_polygons_found, new_arr, new_record)
    new_polygons_found = copy.copy(polygons_found)
    new_arr = copy.copy(arr)
    new_record = copy.copy(record)

    if not polygons_found[4]:
        p7 = heptagonals_begin_with_x(startx)
        if p7:
            for p in p7:
                startp = int(str(p)[-2:])
                if startp >= 10:
                    new_polygons_found[4] = True
                    new_arr = arr + [p]
                    new_record = record + ["hept"]
                    next_polygons(startp, new_polygons_found, new_arr, new_record)
    new_polygons_found = copy.copy(polygons_found)
    new_arr = copy.copy(arr)
    new_record = copy.copy(record)

    pass
    
octagonal_nums = []
for i in range(1000, 10000):
    if octagonals[i]:
        octagonal_nums.append(i)

# Start number
i = 0
l = len(octagonal_nums)
while i < l:
    y = octagonal_nums[i]
    start_arr = [y]
    starty = int(str(y)[-2:])
    start_polygons_found = [False, False, False, False, False, True]
    if starty >= 10:
        start_record = ["oct"]
        good = next_polygons(starty, start_polygons_found, start_arr, start_record)
        if good:
            break
    i += 1


print("...End")