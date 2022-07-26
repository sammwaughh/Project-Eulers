# Problem 13

print("Running...")

file13 = open("13.txt", "r")
strNums = file13.readlines()
sum = 0
for s in strNums:
    sum += int(s.strip())

print(sum)
# Read the first 10 digits

print("...End")
