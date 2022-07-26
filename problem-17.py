# Problem 17
# Number letter counts

print("Running...")

numberWords = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "thousand",
}

numberWordLength = {"and": 3}

for key in numberWords:
    numberWordLength[key] = len(numberWords[key])

def countLetters(n):
    if n < 10:
        return numberWordLength[n]
    elif n < 100:
        units = n % 10
        tens = n - units
        if units != 0:
            return numberWordLength[tens] + numberWordLength[units]
        else:
            return numberWordLength[tens]
    elif n < 1000:
        hundreds = n // 100
        remainder = n - (100*hundreds)
        if remainder == 0:
            return numberWordLength[hundreds] + numberWordLength[100]
        else:
            return numberWordLength[hundreds] + numberWordLength[100] + numberWordLength["and"] + countLetters(n - (100*hundreds))
    else:
        return numberWordLength[1000]
        
sum = 0
for i in range(1, 1001):
    sum += countLetters(i)
print(sum)

print("...End")
