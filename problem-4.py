# Problem 4

print("Running...")

def isPalindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False

largestPal = 101
for i in range(1000):
    for j in range(1000):
        m = i*j
        if isPalindrome(m) and m > largestPal:
            largestPal = m

print(largestPal)

print("...End")
