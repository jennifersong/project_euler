import operator, time

number = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450

ordered = {}

# Sorts the digits in ascending order, then concatenates and returns them as a string
def sorted_concatenation(digits):
	return "".join(map(str, sorted(map(int, digits))))
	
def greatest_product(number):
	start = time.time()
	string = str(number)
	while len(string) >= 5:
		# Current substring to work with are the first five digits of the number
		five = string[0:5]
		reordered_five = sorted_concatenation(five)
		
		# Check if our sorted string and product are in the dict; if not, cache them
		if reordered_five not in ordered:
			ordered[reordered_five] = reduce(operator.mul, map(int, five))
			
		# Trim the first character off the number to check the next five integers' product
		string = string[1:]
		
	elapsed = (time.time() - start)

	print "time: %s seconds" % elapsed	
	return max(ordered.itervalues())
		
print greatest_product(number)