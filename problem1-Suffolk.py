
def threesAndFives(n):
    # suppose n = 10
    # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    ourSum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            ourSum += i
    return ourSum

print(threesAndFives(1000))
