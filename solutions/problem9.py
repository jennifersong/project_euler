def square(x):
	return x*x

def is_pythagorean(a, b, c):
	return (square(a) + square(b)) == square(c)

def pythagorean_sum_equal_to(x):
	for c in range(1, x):
		for b in range(1, c):
			for a in range(1, b):
				if (a + b + c == x) and is_pythagorean(a, b, c):
					return a*b*c
					
print pythagorean_sum_equal_to(1000)