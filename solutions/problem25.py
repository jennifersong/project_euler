fibonacci = {}

def fib(nth):
	if nth <= 2:
		fibonacci[nth] = 1
	else:
	 	fibonacci[nth] = fibonacci[nth-1] + fibonacci[nth-2]
	return fibonacci[nth]
	
def count_digits(num):
	return len(str(num))

def count_fibonacci_digits(num_digits):
	x = 1
	while count_digits(fib(x)) < num_digits:
		x += 1
	return x
	
print count_fibonacci_digits(1000)