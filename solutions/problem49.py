from itertools import permutations, combinations

def is_prime(num):
    for divisor in xrange(2, num):
        if num % divisor == 0:
            return False
    return True
    
def is_sequence(lst):
    difference = lst[1] - lst[0]
    for nth, term in enumerate(lst):
        if nth+1 == len(lst):
            return True
        elif (lst[nth+1] - term) != difference:
            return False

primes = []
for x in xrange(1000, 10000):
    if is_prime(x):
        primes.append(x)

primes_with_permutations = []
# create permutations
for prime in primes:
    grouping = [prime]
    for thing in permutations(str(prime)):
        candidate = int(''.join(thing))
        if candidate in primes and candidate != prime:
            grouping.append(candidate)
            primes.remove(candidate)
    primes_with_permutations.append(grouping)

primes_with_permutations = filter(lambda x: len(x) >= 3, primes_with_permutations)
# groups of primes might be longer than 3, so get combinations of 3
combinations_of_permutations = map(lambda x: list(combinations(x, 3)), primes_with_permutations)

# filter out all combinations for those that are arithmetic sequence
for group in combinations_of_permutations:
    seq = filter(lambda x: is_sequence(sorted(x)), group)
    if seq:
        print seq