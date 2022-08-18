# Problem 97

print("Running...")

# 2^30 = 1073741824
power2 = 1073741824

j = 30
arr = []
while j < 7830457:
    arr.append(power2)
    newPower = power2*2
    power2 = int(str(newPower)[-10:])
    j += 1
num = power2*28433 + 1
print(str(num)[-10:])

print("...End")