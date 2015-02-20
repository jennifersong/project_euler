import math

def is_prime(num):
	for divisor in xrange(2, int(math.sqrt(num))+1):
		if num % divisor == 0:
			return False
	return True
    
print sum((x for x in xrange(2, 2000000) if is_prime(x)))