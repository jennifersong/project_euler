import fractions

denominators = {1: 2}

more_digit_count = 0
for num in xrange(2, 1001):
    denominator = 2 + fractions.Fraction(1, denominators[num-1])
    denominators[num] = denominator
    frac = 1 + fractions.Fraction(1, denominator)
    if len(str(frac.numerator)) > len(str(frac.denominator)):
        more_digit_count += 1
print more_digit_count