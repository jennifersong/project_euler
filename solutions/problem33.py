import fractions

def eliminate_common_digits(a, b):
    fraction_list = []
    a, b = list(str(a)), list(str(b))
    for i, digit_a in enumerate(a):
        for j, digit_b in enumerate(b):
            if digit_a == digit_b:
                clone_a, clone_b = a[::1], b[::1]
                clone_a.pop(i)
                clone_b.pop(j)
                if len(clone_a) > 0 and len(clone_b) > 0 and clone_a[0] != '0' and clone_b[0] != '0':
                    frac = fractions.Fraction(int(clone_a[0]), int(clone_b[0]))
                    fraction_list.append(frac)
    return fraction_list
                
weird_fractions = []
for a in xrange(1, 100):
    for b in xrange(a+1, 100):
        current = fractions.Fraction(a, b)
        if current in eliminate_common_digits(a, b):
            weird_fractions.append([a, b])
weird_fractions = filter(lambda lst: lst[0] % 10 != 0 and lst[1] % 10 != 0, weird_fractions)
weird_fractions = [fractions.Fraction(a, b) for [a, b] in weird_fractions]
print reduce(lambda a, b: a*b, weird_fractions)