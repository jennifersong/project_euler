import csv

words = []
word_values = []
triangle_numbers = []

def calculate_word_value(word):
	return sum(map(calculate_letter_value, word))
	
def calculate_letter_value(letter):
	return ord(letter) - 64

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