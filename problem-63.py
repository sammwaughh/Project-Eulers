# Problem 63

print("Running...")

def digitCount(n):
    return len(str(n))

count = 0
nums = []
for n in range(1, 100):
    base = 1
    done = False
    while not done:
        num = base**n
        digits = digitCount(num)
        if digits == n:
            nums.append(num)
            count += 1
        elif digits > n:
            done = True
        base += 1
        
print(count)

# Works

print("...End")