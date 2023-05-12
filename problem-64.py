# Problem 64
from math import sqrt, floor

print("Running...")

# Root 10
print(3+1/(6+1/(6+1/(6+1/6))))

def find_chain_n(n):
    integer_part, remainder, target = split(n)


def split(x):
    integer_part = floor(x)
    remainder = x - integer_part
    target = 1/remainder
    return integer_part, remainder, target

    
###
### Use paper to work out precise mechanism!
###

print(find_chain_n(23))

print("...End")