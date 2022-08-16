# Problem 45

print("Running...")

ts = []
ps = []
hs = []

def makeNthT(n):
    return (n*(n+1))//2

def makeNthP(n):
    return (n*(3*n - 1))//2

def makeNthH(n):
    return n*(2*n - 1)

for i in range(1, 100000):
    ts.append(makeNthT(i))
    ps.append(makeNthP(i))
    hs.append(makeNthH(i))

for t in ts:
    if t in ps and t in hs:
        print(t)

# Works, takes a min

print("...End")
