import csv

words = []
word_values = []
triangle_numbers = []

AlphabeticalValues = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

def calculate_word_value(word):
	return sum(map(calculate_letter_value, word))
	
def calculate_letter_value(letter):
	return AlphabeticalValues[letter]

def create_words(filename):
	with open(filename, "r") as word_file:
		reader = csv.reader(word_file, delimiter=",")
		for word in reader:
			words.extend(word)
			
def triangle_words(filename):
	create_words(filename)
	word_values = map(calculate_word_value, words)
	generate_triangle_numbers(max(word_values))
	return len(filter(lambda x: x in triangle_numbers, word_values))
	
def generate_triangle_numbers(max_num):
	x = 1
	largest = 0
	while largest <= max_num:
		largest = int(0.5*x*(x+1))
		triangle_numbers.append(largest)
		x += 1
	
print triangle_words("../files/words.txt")