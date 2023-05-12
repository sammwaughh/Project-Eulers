# Problem 62

print("Running...")

def is_anagram(a, b):
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




print("...End")