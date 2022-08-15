# Problem 31

from audioop import add


print("Running...")

def isSameSet(A, B):
    ASorted = sorted(A)
    BSorted = sorted(B)
    if ASorted == BSorted:
        return True
    else:
        return False

def distinctSet(S):
    newS = []
    for ele in S:
        sortedEle = sorted(ele)
        if sortedEle not in newS:
            newS.append(sortedEle)
    return newS

def addingCombos(target, set):
    #print(target)
    combos = []
    for ele in set:
        if ele == target:
            combos.append([ele])
        elif ele < target:
            for ele2 in addingCombos(target - ele, set):
                combos.append([ele] + ele2)
    return combos

#print(len(addingCombos(10, [1,2,5,10])))
a = distinctSet(addingCombos(200, [200,100,50,20,10]))
count = 0
for ele in a:
    if 10 in ele:
        count += 1
print(count)

"""coinPerms = []
def addCoins(a, b, c, d):
    return a + 2*b + 5*c + 10*d

for a in range(11):
    for b in range(6):
        for c in range(3):
            for d in range(2):
                if a + 2*b + 5*c + 10*d == 10:
                    coinPerms.append((a, b, c, d))"""

"""total = 0
for h in range(201):
    print(h)
    for g in range(101):
        for f in range(41):
            for a in range(21):
                for b in range(11):
                    for c in range(5):
                        for d in range(3):
                            for e in range(2):
                                if h + 2*g + 5*f + 10*a + 20*b + 50*c + 100*d + 200*e == 200:
                                    total += 1

print(total)"""

"""t = 0
a = 0
aStop = False
while a <= 1 and not aStop:
    s = 200*a
    if s > 200:
        aStop = True
    else:
        b = 0
        bStop = False
        while b <= 2 and not bStop:
            s = 200*a + 100*b
            if s > 200:
                bStop = True
            else:
                c = 0
                cStop = False
                while c <= 4 and not cStop:
                    s = 200*a + 100*b+ 50*c
                    if s > 200:
                        cStop = True
                    else:
                        d = 0
                        dStop = False
                        while d <= 10 and not dStop:
                            s = 200*a + 100*b+ 50*c + 20*d
                            if s > 200:
                                dStop = True
                            else:
                                e = 0
                                eStop = False
                                while c <= 20 and not eStop:
                                    s = 200*a + 100*b+ 50*c + 20*d + 10*c
                                    if s > 200:
                                        eStop = True
                                    else:
                                        f = 0
                                        fStop = False
                                        while f <= 40 and not fStop:
                                            s = 200*a + 100*b+ 50*c + 20*d + 10*c + 5*f
                                            if s > 200:
                                                fStop = True
                                            else:
                                                g = 0
                                                gStop = False
                                                while g <= 100 and not gStop:
                                                    s = 200*a + 100*b+ 50*c + 20*d + 10*c + 5*f + 2*c
                                                    if s > 200:
                                                        gStop = True
                                                    else:
                                                        h = 0
                                                        hStop = False
                                                        while h <= 200 and not hStop:
                                                            s = 200*a + 100*b+ 50*c + 20*d + 10*c + 5*f + 2*c + h
                                                            if s > 200:
                                                                hStop = True
                                                            elif s == 200:
                                                                t += 1
                                                            h += 1
                                                        g += 1
                                                f += 1
                                        e += 1
                                d += 1
                        c += 1
                b += 1
        a += 1

print(t)"""

print("...End")
