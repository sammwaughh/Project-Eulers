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
    print(nums)
    print(suits)
    isFlush = isSameSuit(suits)
    isStraight = isStraightFunc(nums)
    print(isStraight)

    
# ['7D', '2S', '5D', '3S', 'AC']
evalHand(['4D', '2D', '5D', '3S', 'AD'])

def compareHands(hand):
    hand1 = hand[:5]
    hand2 = hand[5:]
    print(hand1, hand2)


print("...End")