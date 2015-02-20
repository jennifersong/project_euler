import math

def is_prime(num):
	for divisor in xrange(2, int(math.sqrt(num))+1):
		if num % divisor == 0:
			return False
	return True
    
prime_count = 0
current = 1
while prime_count < 10001:
    current += 1
    if is_prime(current):
        prime_count += 1
    
print current