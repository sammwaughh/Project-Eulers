# Problem 700

print("Running...")

def nthEulerCoin(n):
    return (1504170715041707*n)%4503599627370517

sum = 1517926264989119
i = 1000000000
smallestCoin = 14578937
bound = 2000000000
while i <= bound:
    eulerCoin = nthEulerCoin(i)
    if eulerCoin < smallestCoin:
        smallestCoin = eulerCoin
        sum += eulerCoin
    i += 1

print(sum)
print(smallestCoin)

print("...End")