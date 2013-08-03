import math

def is_prime(num):
	for divisor in xrange(2, num):
		if num % divisor == 0:
			return False
	return True
	
def divisors(num):
	return filter(lambda x: num % x == 0, xrange(2, int(math.sqrt(num))))
	
def prime_divisors(num):
	return filter(is_prime, divisors(num))
	
print max(prime_divisors(600851475143))