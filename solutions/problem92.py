digit_chains = {1: 1, 89: 89}

def square_digits(num):
    return sum((pow(int(n), 2) for n in str(num)))

def exhaust_chain(num):
    if num in digit_chains:
        return digit_chains[num]
    else:
        digit_chains[num] = exhaust_chain(square_digits(num))
    return digit_chains[num]

# note: takes 54 seconds to run
for num in xrange(1, 10000000):
    exhaust_chain(num)
print sum(1 for i in (key for key, value in digit_chains.iteritems() if value == 89))