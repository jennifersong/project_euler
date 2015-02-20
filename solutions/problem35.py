import math

def is_prime(num):
	for divisor in xrange(2, int(math.sqrt(num))+1):
		if num % divisor == 0:
			return False
	return True
    
def is_all_prime(num_lst):
    for num in num_lst:
        if not is_prime(num):
            return False
    return True
    
def is_prime_digits(num):
    return len(str(num)) == 1 or set(['2', '4', '5', '6', '8', '0']).intersection(set(str(num))) == set()
    
def generate_rotations(num):
    rotations = []
    digits = list(str(num))
    for x in xrange(len(digits)):
        digit = digits.pop(0)
        digits.append(digit)
        rotations.append(int(''.join(digits)))
    return rotations
    
primes = [x for x in xrange(2, 1000001) if is_prime(x) and is_prime_digits(x)]
prime_count = 0

for prime in primes:
    prime_perms = generate_rotations(prime)
    if is_all_prime(prime_perms):
        prime_count += 1
print prime_count