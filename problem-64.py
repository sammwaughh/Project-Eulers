# Problem 64
from math import sqrt, floor

print("Running...")

def find_chain_n(n):
    i = 0
    start, target = split(n)
    sequence = []
    while i < 16:
        integer_part, target = split(target)
        sequence.append(integer_part)
        i += 1
        
    return (start,sequence)
    
def split(x):
    integer_part = floor(x)
    remainder = x - integer_part
    new_target = 1/remainder
    return integer_part, new_target

print(find_chain_n(sqrt(23)))

print("...End")