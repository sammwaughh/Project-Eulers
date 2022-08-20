# Problem 54

from re import L


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
            numsHighA.append(14)
        elif num == 'T':
            numsLowA.append(10)
            numsHighA.append(10)
        elif num == 'J':
            numsLowA.append(11)
            numsHighA.append(11)
        elif num == 'Q':
            numsLowA.append(12)
            numsHighA.append(12)
        elif num == 'K':
            numsLowA.append(13)
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
        countArr = [0]*15
        for n in nums:
            if n == 'A':
                n = '14'
            if n == 'K':
                n = '13'
            if n == 'Q':
                n = '12'
            if n == 'J':
                n = '11'
            if n == 'T':
                n = '10'
            countArr[int(n)] += 1
        if 4 in countArr:
            return ('four of a kind', (countArr.index(4), countArr.index(1)))
        if 3 in countArr and 2 in countArr:
            return ('full house', (countArr.index(3), countArr.index(2)))
        if 3 in countArr:
            k = countArr.index(1)
            l = countArr.index(1, k+1, 15)
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
                k = countArr.index(1, j+1, 15)
                l = countArr.index(1, k+1, 15)
                return ('pair', (i, j, k, l))
        else:
            a = countArr.index(1)
            b = countArr.index(1, a+1, 15)
            c = countArr.index(1, b+1, 15)
            d = countArr.index(1, c+1, 15)
            e = countArr.index(1, d+1, 15)
            return ('high card', (a,b,c,d,e))
    
# ['7D', '2S', '5D', '3S', 'AC']
#print(evalHand(['2C', 'KD', '2S', 'KS', 'KH']))

handDict = {
    'high card': 0,
    'pair': 1,
    'two pair': 2,
    'three of a kind': 3,
    'straight': 4,
    'flush': 5,
    'full house': 6,
    'four of a kind': 7,
    'straight flush': 8
}

def compareHands(hand):
    hand1 = hand[:5]
    hand2 = hand[5:]
    hand1Eval = evalHand(hand1)
    hand2Eval = evalHand(hand2)
    handScore1 = handDict[hand1Eval[0]]
    handScore2 = handDict[hand2Eval[0]]
    print(hand1, hand2)
    print(evalHand(hand1), evalHand(hand2))
    print(handScore1, handScore2)
    if handScore1 > handScore2:
        return 1
    elif handScore1 < handScore2:
        return 2
    else:
        player1 = hand1Eval[1]
        player2 = hand2Eval[1]
        if handScore1 == 0:
            i = 4
            while True:
                p1 = player1[i]
                p2 = player2[i]
                if p1 > p2:
                    return 1
                elif p2 > p1:
                    return 1
                else:
                    i -= 1
        elif handScore1 == 1:
            if player1[0] > player2[0]:
                return 1
            elif player2[0] > player1[0]:
                return 2
            else:
                



compareHands(hands[1])

print("...End")