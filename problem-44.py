# Problem 44

print("Running...")

def genPentagonals(n):
    pents = []
    for i in range(1, n+1):
        pents.append((3*i*i - i)//2)
    return pents

pents = genPentagonals(3000)

smallestD = 0
for i in range(len(pents)):
    for j in range(i+1, len(pents)):
        d = pents[j] - pents[i]
        if d in pents:
            s = pents[j] + pents[i]
            if s in pents:
                if d < smallestD or smallestD == 0:
                    smallestD = d
print(smallestD)
# Works. Trial and Error finds answer works 
# for below 3000th pentagonal number
# Takes a minute

print("...End")
