# Problem 19

print("Running...")

# list of 0s and 1s where 0 represents not first of the month and 1 represents it is first of the month
# first index denotes 1 Jan 1901 and last index represents 31 Dec 2000
# there should be 12 * 100 = 1200 1s. Hence sum(firstOMonth) == 1200

start = [1]
thirtyMonth0 = [0] * 29
thirtyMonth = start + thirtyMonth0
thrityOneMonth0 = [0] * 30
thirtyOneMonth = start + thrityOneMonth0

def addThirtyMonth(dayList):
    return dayList + thirtyMonth

def addThirtyOneMonth(dayList):
    return dayList + thirtyOneMonth







print("...End")
