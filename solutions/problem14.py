collatz_hash = {1: 1}

def collatz(n):
	x = n		# Save the original value of n
	count = 0
	
	# Compute the length of the Collatz sequence for x
	while n > 0:
		# if n is in the hash table, its sequence length is cached, so we can add the current sequence length to 
		# the cached sequence length to get the total sequence length for collatz(x)
		if n in collatz_hash:
		 	count = count + collatz_hash[n]
		 	break
		count += 1	# We didn't find the cached value, so length of sequence goes up by 1
		if is_odd(n):
			n = 3*n + 1
		elif is_even(n):
			n = n/2
		
	x_length = count	# Save this value to return
	
	# Cache the Collatz sequence values for all other numbers in the Collatz sequence for n
	while x not in collatz_hash:
		if x < 1000000:		# We don't want to cache any numbers above 1000000
			collatz_hash[x] = count
		if is_odd(x):
			x = 3*x + 1
		elif is_even(x):
			x = x/2
		count -= 1

	return x_length
	
def is_odd(n):
	return n % 2 == 1
	
def is_even(n):
	return n % 2 == 0
	
def stuff():
	largest = 1
	max_len = 1
	for x in range(1, 1000000):
		current = collatz(x)
	 	if current > max_len:
			largest = x
		 	max_len = current
 	return largest

print stuff()
			