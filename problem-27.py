# Problem 27

print("Running...")

difference = 2
top = 1001*1001
i = 1
diagonals = []
count = 0
while i <= top:
    diagonals.append(i)
    i += difference
    count += 1
    if count % 4 == 0:
        difference += 2

print(sum(diagonals))

print("...End")
