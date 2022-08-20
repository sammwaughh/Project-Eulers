# Problem 54

print("Running...")

file54 = open("54.txt", "r")
arr = file54.read().split("\n")
arr2 = []
for ele in arr:
    arr2.append(ele.split(" "))
hands = arr2[:-1]

def isSameSuit(suits):
    sameSuits = True
    suit0 = suits[0]
    i = 1
    while sameSuits and i < 5:
        if suits[i] != suit0:
            sameSuits = False
        i += 1
    return sameSuits

def isStraightFunc(nums):
    numsLowA = []
    numsHighA = []
    for num in nums:
        if num == 'A':
            numsLowA.append(1)
            numsHighA.append(13)
        else:
            numsLowA.append(int(num))
            numsHighA.append(int(num))
    numsLowA.sort()
    numsHighA.sort()
    num0 = numsLowA[0]
    isStraightLow = True
    i = 1
    while isStraightLow and i < 5:
        if numsLowA[i] != num0+i:
            isStraightLow = False
        i += 1
    if isStraightLow:
        return True
    else:
        num0 = numsHighA[0]
        isStraightHigh = True
        i = 1
        while isStraightHigh and i < 5:
            if numsHighA[i] != num0+i:
                isStraightHigh = False
            i += 1
        if isStraightHigh:
            return True
        else:
            return False

def evalHand(hand):
    nums = []
    suits = []
    for card in hand:
        nums.append(card[0])
        suits.append(card[1])
    isFlush = isSameSuit(suits)
    isStraight = isStraightFunc(nums)
    if isStraight:
        if isFlush:
            return ('straight flush', nums)
        else:
            return ('straight', nums)
    elif isFlush:
        return ('flush', nums)
    else:
        countArr = [0]*14
        for n in nums:
            if n == 'A':
                n = '13'
            countArr[int(n)] += 1
        if 4 in countArr:
            return ('four of a kind', (countArr.index(4), countArr.index(1)))
        if 3 in countArr and 2 in countArr:
            return ('full house', (countArr.index(3), countArr.index(2)))
        if 3 in countArr:
            k = countArr.index(1)
            l = countArr.index(1, k+1, 14)
            return ('three of a kind', (countArr.index(3), k, l))
        if 2 in countArr:
            i = countArr.index(2)
            countArr[i] = 0
            if 2 in countArr:
                j = countArr.index(2)
                k = countArr.index(1)
                return ('two pair', (i, j, k))
            else:
                j = countArr.index(1)
                k = countArr.index(1, j+1, 14)
                l = countArr.index(1, k+1, 14)
                return ('pair', (i, j, k, l))
        else:
            a = countArr.index(1)
            b = countArr.index(1, a+1, 14)
            c = countArr.index(1, b+1, 14)
            d = countArr.index(1, c+1, 14)
            e = countArr.index(1, d+1, 14)
            return ('high card', (a,b,c,d,e))

                   

    
# ['7D', '2S', '5D', '3S', 'AC']
print(evalHand(['AC', '8D', '8S', 'AS', 'AH']))

def compareHands(hand):
    hand1 = hand[:5]
    hand2 = hand[5:]
    print(hand1, hand2)


print("...End")