# Problem 59

print("Running...")

def xor(a, b):
    bina = bin(a)
    binb = bin(b)
    ans = int(bina, 2) ^ int(binb, 2)
    return int(ans)

file59 = open("59.txt", "r")
encrypted0 = file59.read().split(",")
encrypted = []
for ele in encrypted0:
    encrypted.append(int(ele))

commons = ['and', 'or', 'the', 'is', 'who', 'how']
keys = []
for i in range(26):
    for j in range(26):
        for k in range(26):
            key = [i+97, j+97, k+97]
            keys.append(key)

x = 26**2
realKey = None
for i in range(len(keys)):
    key = keys[i]
    longKey = key*485
    plain = []
    for i in range(1455):
        plain.append(xor(longKey[i], encrypted[i]))
    plainString = ""
    for ele in plain:
        plainString += chr(ele)
    valid = True
    for word in commons:
        if word not in plainString:
            valid = False
    if valid:
        realKey = key

realLongKey = realKey*485
plain = []
for i in range(1455):
    plain.append(xor(realLongKey[i], encrypted[i]))
plainString = ""
for ele in plain:
    plainString += chr(ele)
#print(plainString)
print(sum(plain))

print("...End")