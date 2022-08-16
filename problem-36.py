# Problem 36

print("Running...")

def isPalindrome(s):
    r = ""
    for i in range(len(s)-1, -1, -1):
        r += s[i]
    if r == s:
        return True
    else:
        return False

def makeBin(n):
    return str(bin(n))[2:]

sum = 0
for i in range(1000000):
    if isPalindrome(str(i)):
        if isPalindrome(makeBin(i)):
            sum += i
print(sum)


print("...End")
