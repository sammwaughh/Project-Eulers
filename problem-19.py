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
monthDays = [None,31,28,31,30,31,30,31,31,30,31,30,31]

def addDays(month, dayList):
    return dayList + [1] + [0]*(monthDays[month]-1)

year = 1901
days = []

while year <= 2000:
    if year % 4 == 0:
        monthDays[2] = 29
    else:
        monthDays[2] = 28
    month = 1
    while month <= 12:
        days = addDays(month, days)
        month += 1
    year += 1

# 1 Jan 1901 was a Tuesday => 6 Jan 1901 was a Sunday
# Index 5, 12, 19, ... are Sundays

count = 0
i = 5
l = len(days)
while i < l:
    if days[i] == 1:
        count += 1
    i += 7

print(count)

print("...End")
