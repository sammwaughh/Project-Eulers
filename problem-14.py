# Problem 14

print("Running...")

# Define a simple Collatz function
def nextCollatz(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3*n + 1

# Define dictionary
# Keys are starting numbers
# Values are the length of the sequence they produce
numsDict = {}

# Initialize base case
numsDict[1] = 1

def collatzLength(n):
    if n in numsDict:
        return numsDict[n]
    else:
        value = 1 + collatzLength(nextCollatz(n))
        numsDict[n] = value
        return value

longestSequenceLength = 1
startingNumber = 1
for i in range(1, 1000000):
    sequenceLength = collatzLength(i)
    if sequenceLength > longestSequenceLength:
        longestSequenceLength = sequenceLength
        startingNumber = i

print(longestSequenceLength, startingNumber)

print("...End")
