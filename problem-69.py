# Problem 69

print("Running...")

def is_relative_prime(x, n):
    if x == 1:
        return True
    for i in range(2, x+1):
        if x % i == 0 and n % i == 0:
            return False
    return True

def totient(n):
    count = 1
    for i in range(2, n):
        if is_relative_prime(i, n):
            count += 1
    return count

def totient2(n):
    pass

for i in range(2,2000):
    if i % 100 == 0:
        print(i)
    temp = totient(i)

print("...End")

