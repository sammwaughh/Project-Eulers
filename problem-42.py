# Problem 42

print("Running...")

words = open("42.txt", "r")
wordList = words.read()[1:-1].split("\",\"")
words.close()

ts = [1]
i = 2
while ts[-1] < 300:
    ts.append(ts[-1]+i)
    i += 1

def wordValue(word):
    sum = 0
    for c in word:
        sum += ord(c) - 64
    return sum

count = 0
for word in wordList:
    if wordValue(word) in ts:
        count += 1

print(count)

print("...End")
