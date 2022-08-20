# Problem 686

print("Running...")

def firstThreeDigits(n):
    return int(str(n)[:3])

count = 0
j = 1
while count < 678910:
    if firstThreeDigits(2**j) == 123:
        count += 1
        print(count)
    j += 1
print(j-1)

print("...End")