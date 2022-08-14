# Problem 25

print("Running...")

def numDigits(n):
    s = str(n)
    return len(s)

a = 1
b = 1
i = 2
stop = False
while not stop:
    if numDigits(b) == 1000:
        print(i, b)
        stop = True
    else:
        t = a + b
        a = b
        b = t
        i += 1

print("...End")
