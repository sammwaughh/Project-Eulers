# Problem 28

print("Running...")

powers = []
for i in range(2, 101):
    for j in range(2, 101):
        k = i**j
        if k not in powers:
            powers.append(k)

print(len(powers))

print("...End")
