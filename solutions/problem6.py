def square(x):
	return x*x
	
def square_of_sums(lst):
	return square(sum(lst))
	
def sum_of_squares(lst):
	return sum(map(square, lst))
	
print square_of_sums(range(101)) - sum_of_squares(range(101))