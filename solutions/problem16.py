import math

def sum_digits(x, y):
	return sum(map(int, str(int(math.pow(x, y)))))

print sum_digits(2, 1000)