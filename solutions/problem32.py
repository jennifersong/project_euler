identities = {}
pandigital_lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def is_pandigital(strng):
    return sorted(strng) == pandigital_lst
    
def get_lengths(num):
    length = len(str(num))
    if length == 1:
        return (3, 4)
    if length == 2:
        return (2, 3)
    if length == 3:
        return (1, 2)
    if length == 4:
        return (0, 1)

def get_pandigital_products(num):
    start_length, end_length = get_lengths(num)
    for x in xrange(pow(10, start_length), pow(10, end_length)):
        if can_be_pandigital(x):
            product = x * num
            if product not in identities:
                strng = str(product) + str(x) + str(num)
                if is_pandigital(strng):
                    identities[product] = strng
    
def can_be_pandigital(num):
    return num % 5 != 0   # numbers ending in 5 and 0 can't create pandigital identities
    
for x in xrange(2, 10000):
    if can_be_pandigital(x):
        get_pandigital_products(x)
print sum(identities.iterkeys())
    