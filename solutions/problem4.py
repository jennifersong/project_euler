palindrome = {}

def is_palindrome(num):
	num_str = str(num)
	while len(num_str) >= 2:
		first_char = num_str[0]
		last_char = num_str[len(num_str)-1]
		if first_char != last_char:
			return False
		else:
			num_str = num_str[1:len(num_str)-1]
	return True

def highest_palindrome_product(maximum):
	for x in range (1, maximum):
		for y in range (1, maximum):
			product = x*y
			if product not in palindrome:
				palindrome[product] = is_palindrome(product)
	filtered_palindrome = dict((key, value) for key, value in palindrome.iteritems() if value == True)
	return max(filtered_palindrome.keys(), key=int)
	
print highest_palindrome_product(1000)