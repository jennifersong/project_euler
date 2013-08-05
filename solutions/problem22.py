import re

AlphabeticalValues = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

def names_value_sum(filename):
	names = open(filename)
	sorted_list = sorted(re.split(',', re.sub('\"', '', names.read())))
	
	nth = 1
	total = 0
	for name in sorted_list:
		sum = 0
		for letter in name:
			sum += AlphabeticalValues[letter]
		total += sum * nth
		nth += 1
	names.close()
	return total
	
print names_value_sum("names.txt")