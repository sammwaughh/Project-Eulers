# Problem 51

print("Running...")

### Efficient Prime list generator

from math import isqrt

def primes_less_than(n):
    if n <= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, isqrt(n)+1):
        if is_prime[i]:
            for x in range(i*i, n, i):
                is_prime[x] = False
    return is_prime

def generate_boolean_combinations(n):
    if n == 0:
        return [[]]
    else:
        sub_combinations = generate_boolean_combinations(n - 1)
        combinations = []
        for item in sub_combinations:
            combinations.append(item + [True])
            combinations.append(item + [False])
        return combinations

# True/False primes under 100,000
prime_bools = primes_less_than(1000000)
prime_nums = [i for i in range(len(prime_bools)) if prime_bools[i]]

# A number is 0-9 or *
digits = ['0','1','2','3','4','5','6','7','8','9']

# True/False combinations
boolean_combinations = generate_boolean_combinations(6)

# True/False combinations with 2 Trues
bool1 = []
bool2 = []
bool3 = []
bool4 = []
bool5 = []
for combo in boolean_combinations:
    c = 0
    for b in combo:
        if b:
            c += 1
    if c == 1:
        bool1.append(combo)
    elif c == 2:
        bool2.append(combo)
    elif c == 3:
        bool3.append(combo)
    elif c == 4:
        bool4.append(combo)
    elif c == 5:
        bool5.append(combo)

def make_strNum(digits, combo):
    i = 0
    strNum = ""
    for b in combo:
        if b:
            strNum += '*'
        else:
            strNum += digits[i]
            i += 1
    return strNum

digit_list_1 = digits.copy()
big_list_1 = []
for digits in digit_list_1:
    star_list = []
    for combo in bool5:
        star_list.append(make_strNum(digits, combo))
    big_list_1.append(star_list)


digits = ['0','1','2','3','4','5','6','7','8','9']
digit_list_2 = []
for j in range(1, 10):
        for k in range(10):
            digit = digits[j] + digits[k]
            digit_list_2.append(digit)
big_list_2 = []
for digits in digit_list_2:
    star_list = []
    for combo in bool4:
        star_list.append(make_strNum(digits, combo))
    big_list_2.append(star_list)


digits = ['0','1','2','3','4','5','6','7','8','9']
digit_list_3 = []
for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            digit = digits[i] + digits[j] + digits[k]
            digit_list_3.append(digit)
big_list_3 = []
for digits in digit_list_3:
    star_list = []
    for combo in bool3:
        star_list.append(make_strNum(digits, combo))
    big_list_3.append(star_list)


digits = ['0','1','2','3','4','5','6','7','8','9']
digit_list_4 = []
for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                digit = digits[i] + digits[j] + digits[k] + digits[l]
                digit_list_4.append(digit)
big_list_4 = []
for digits in digit_list_4:
    star_list = []
    for combo in bool2:
        star_list.append(make_strNum(digits, combo))
    big_list_4.append(star_list)


digits = ['0','1','2','3','4','5','6','7','8','9']
digit_list_5 = []
for i in range(1, 10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                for m in range(10):
                    digit = digits[i] + digits[j] + digits[k] + digits[l] + digits[m]
                    digit_list_5.append(digit)
big_list_5 = []
for digits in digit_list_5:
    star_list = []
    for combo in bool1:
        star_list.append(make_strNum(digits, combo))
    big_list_5.append(star_list)


def replace_star(star_num, digit):
    return int(star_num.replace('*', str(digit)))

flat_list = []
mega_list = big_list_1 + big_list_2 + big_list_3 + big_list_4 + big_list_5
for sub_list in mega_list:
    for ele in sub_list:
        flat_list.append(ele)

print(len(flat_list))
strNums_7 = []

digits = [0,1,2,3,4,5,6,7,8,9]

for strNum in flat_list:
    c = 0
    l = []
    for d in digits:
        number = replace_star(strNum, d)
        if prime_bools[number]:
            c += 1
            l.append(number)
    if c == 8:
        print(strNum)
        print(l)

print("...End")


