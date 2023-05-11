from fractions import Fraction

def digitLength(n):
    return len(str(n))

def do_better_root(fraction):
    t = fraction + Fraction(1, 1)
    r = Fraction(t.denominator, t.numerator)
    return r + Fraction(1, 1)

i = 1
f = Fraction(1, 1)
count = 0
while i < 1001:
    f = do_better_root(f)
    if digitLength(f.numerator) > digitLength(f.denominator):
        count += 1
    i += 1
print(count)

