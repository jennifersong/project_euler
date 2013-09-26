import math

# 1 through 10 don't need to be listed as they all divide into one of the following
divisors = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def is_divisible_by(num, divisor):
	return num % divisor == 0
	
def is_divisible_by_all(num, divisor_lst):
	for divisor in divisor_lst:
		if not is_divisible_by(num, divisor):
			return False
	return True
	
def find_lcm(divisor_lst, increment):
	start = increment
	while not is_divisible_by_all(start, divisor_lst):
		start += increment # need to increment by at least this much for next lcm
	return start
		
print find_lcm(divisors, 2520) # 2520 is lcm of 1-10