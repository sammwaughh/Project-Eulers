# Problem 55

print("Running...")

def isPalindrome(n):
    s = str(n)
    s2 = ""
    for i in range(len(s)-1,-1,-1):
        s2 += s[i]
    if s == s2:
        return True
    else:
        return False

def flipAdd(n):
    s = str(n)
    s2 = ""
    for i in range(len(s)-1,-1,-1):
        s2 += s[i]
    return n + int(s2)

def isLychrel(n):
    i = 0
    while i <= 50:
        n = flipAdd(n)
        if isPalindrome(n):
            return False
        i += 1
    return True

count = 0
for i in range(10001):
    if isLychrel(i):
        count += 1
print(count)

print("...End")