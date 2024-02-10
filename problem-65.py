
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def fractionAddition(f1, f2):
    n1 = f1[0]
    d1 = f1[1]
    n2 = f2[0]
    d2 = f2[1]
    bigd = d1*d2
    top1 = n1*d2
    top2 = n2*d1
    top = top1 + top2
    g = gcd(bigd, top)
    n = top // g
    d = bigd // g
    return (n, d)

def reciprocal(f):
    return (f[1], f[0])

def evaluateContinuedFraction(arr0):
    start = (arr0[0], 1)
    arr = arr0[1:-1]
    val = (1, arr0[-1])
    for i in range(len(arr) - 1, -1, -1):
        x = (arr[i], 1)
        val = reciprocal(fractionAddition(x, val))
    val = fractionAddition(start, val)
    return val
    
def sumOfDigits(n):
    sum = 0
    while n != 0:
        rem = n % 10
        sum += rem
        n -= rem
        n = n // 10
    return sum    

def generateESequence(n):
    arr = [2, 1]
    while len(arr) < n:
        arr.append(1)
    i = 2
    k = 2
    while i < n:
        arr[i] = k
        k += 2
        i += 3
    return arr

numerator, denominator = evaluateContinuedFraction(generateESequence(100))
print(sumOfDigits(numerator))

# Correct