# Problem 58

print("Running...")

### The Seive of Eratosthenes

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

# True/False primes under 1,000,000,000
prime_bools = primes_less_than(1000000000)
prime_nums = [i for i in range(len(prime_bools)) if prime_bools[i]]

print("Done calculating primes")

"""
def grow_square(square):
    size = len(square)
    digit = square[-1][-1] + 1
    for i in range(size-1, -1, -1):
        square[i].append(digit)
        digit += 1
    top = [i for i in range(digit+size+1, digit-1, -1)]
    digit += size + 2
    for i in range(size):
        square[i] = [digit] + square[i]
        digit += 1
    bottom = [i for i in range(digit, digit+size+2)]
    new_square = [top]
    for row in square:
        new_square.append(row)
    new_square.append(bottom)
    return new_square

def grow_square_n_times(square, n):
    for i in range(n):
        square = grow_square(square)
    return square

def print_square(square):
    for row in square:
        print(row)

def return_diagonals(square):
    size = len(square)
    diagonals = []
    for i in range(size):
        diagonals.append(square[i][i])
        if i != size-i-1:
            diagonals.append(square[i][size-i-1])
    return diagonals

side_length = 1
stop = False
my_square = [[1]]

while not stop:
    if side_length % 1001 == 0:
        print(side_length)
    my_square = grow_square(my_square)
    side_length += 2
    diagonals = return_diagonals(my_square)
    l = side_length*2 - 1
    p = 0
    for ele in diagonals:
        if prime_bools[ele]:
            p += 1
    if p / l < 0.1:
        stop = True
print(side_length)"""

def calc_north_east(n):
    return 4*n*n - 10*n + 7

def calc_north_west(n):
    return 4*n*n - 8*n + 5

def calc_south_west(n):
    return 4*n*n - 6*n + 3

side_length = 3
stop = False
p = 0
while not stop:
    side_length += 2
    n = (side_length + 1) // 2
    if prime_bools[calc_north_east(n)]:
        p += 1
    if prime_bools[calc_north_west(n)]:
        p += 1
    if prime_bools[calc_south_west(n)]:
        p += 1

    l = side_length*2 - 1
    ratio = p / l
    print("Side length:{}\tRatio:{}".format(side_length, ratio))

    if ratio < 0.1:
        stop = True
        print(side_length)
    
print("...End")