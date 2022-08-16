# Problem 40

print("Running...")

bigs = ""
i = 1
while len(bigs) < 1000000:
    bigs += str(i)
    i += 1

val = int(bigs[0]) * int(bigs[9]) * int(bigs[99]) * int(bigs[999]) * int(bigs[9999]) * int(bigs[99999]) * int(bigs[999999])
print(val)

print("...End")
