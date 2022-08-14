# Problem 30

print("Running...")

# Guessed that there are none over 1 million
# Sort of hackish

def isFivePowerSum(n):
    s = str(n)
    total = 0
    for c in s:
        total += int(c)**5
    if total == n:
        return True
    else:
        return False

sum = 0
for i in range(2,1000000):
    if isFivePowerSum(i):
        sum += i

print(sum)

print("...End")
