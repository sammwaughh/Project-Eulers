# Problem 62

print("Running...")

def is_anagram_nums(num_a, num_b):
    a = str(num_a)
    b = str(num_b)
    count_a = {}
    count_b = {}
    for c in a:
        if c in count_a.keys():
            count_a[c] += 1
        else:
            count_a[c] = 1
    for c in b:
        if c in count_b.keys():
            count_b[c] += 1
        else:
            count_b[c] = 1
    return count_a == count_b

def first_n_cubes(n):
    arr = []
    i = 1
    while i <= n:
        arr.append(i**3)
        i += 1
    return arr

L = 10000
cubes = first_n_cubes(L)
found = []

for i in range(L):
    cube1 = cubes[i]
    for j in range(i+1, L):
        cube2 = cubes[j]
        if is_anagram_nums(cube1, cube2):
            for k in range(j+1, L):
                cube3 = cubes[k]
                if is_anagram_nums(cube1, cube3):
                    # print(i, j, k)
                    # print(cube1, cube2, cube3)
                    for l in range(k+1, L):
                        cube4 = cubes[l]
                        if is_anagram_nums(cube1, cube4):
                            for m in range(l+1, L):
                                cube5 = cubes[m]
                                if is_anagram_nums(cube1, cube5):
                                    found.append([i+1,j+1,k+1,l+1,m+1])

flat_found = []
for sub_list in found:
    for ele in sub_list:
        flat_found.append(ele)

print(min(flat_found)**3)

print("...End")