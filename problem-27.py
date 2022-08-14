# Problem 27

print("Running...")

difference = 2
top = 5*5
i = 1
diagonals = []
count = 0
while i < top:
    diagonals.append(i)
    i += difference
    count += 1
    if count % 4 == 0:
        difference += 2
print(diagonals)

print("...End")
