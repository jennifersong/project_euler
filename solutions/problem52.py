from collections import Counter

def num_digits_multiples_same(num):
    return len(str(num)) == len(str(num*6))
    
def digits_multiples_same(num):
    digits = Counter(str(num))
    count = 2
    while count <= 6:
        if Counter(str(num * count)) != digits:
            return False
        count += 1
    return True

for x in xrange(1, 1000000):
    if num_digits_multiples_same(x) and digits_multiples_same(x):
        print x
        exit(0)