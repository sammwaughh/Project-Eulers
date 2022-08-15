# Problem 31

print("Running...")

def addNewCoin(list, coin):
    newList = []
    for i in range(len(list)):
        if i < coin:
            newList.append(list[i])
        else:
            newVal = newList[i-coin] + list[i]
            newList.append(newVal)
    return newList

coinList = [1]*201
coins = [2,5,10,20,50,100,200]
for coin in coins:
    coinList = addNewCoin(coinList, coin)
print(coinList[-1])

print("...End")
