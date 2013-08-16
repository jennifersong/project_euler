factorials = {0: 1}
sums = {}

def factorial(num):
	if num not in factorials:
		x = 1
		while x <= num:
			if x not in factorials:
				factorials[x] = factorials[x-1] * x
	 		x += 1
	return factorials[num]

def trim_last_digit(str_num):
	return str_num[0:-1]
	
def sum_factorial_digits(num):
	str_num = str(num)
	if len(str_num) <= 1:
		sums[num] = factorial(num)
	else:
		sums[num] = sums[int(trim_last_digit(str_num))] + factorial(int(str_num[-1]))
	return sums[num]

def factorions_sum(num):
	return sum(filter(lambda y: len(str(y)) > 1, [x for x in range(num) if sum_factorial_digits(x) == x]))
	
# 9!*6 > 999999 but 9!*7 < 9999999 so max digits in "all numbers" is 7
print factorions_sum(1000000)