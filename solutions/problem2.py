fibonacci = {}

def fib(nth):
	result = 0
	if nth <= 2:
		fibonacci[nth] = nth
	else:
	 	result = fibonacci[nth-1] + fibonacci[nth-2]
		# Don't cache any values above 4 million
		if result < 4000000:
			fibonacci[nth] = result
	return result

def is_even(num):
	return num % 2 == 0

def stuff():
	x = 1
	while fib(x) < 4000000:
		x += 1
	return sum(list(value for key, value in fibonacci.iteritems() if is_even(value)))
	
print stuff()