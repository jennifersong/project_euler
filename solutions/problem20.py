import math

def sum_digits(x):
	return sum(map(int, str(int(math.factorial(x)))))
	
print sum_digits(100)