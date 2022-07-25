# Problem 6

print("Running...")

sumOfSquares = 0
sum = 0
for i in range(101):
    sumOfSquares += i**2
    sum += i

print(abs(sum**2 - sumOfSquares))

print("...End")
