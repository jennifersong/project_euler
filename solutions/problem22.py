import csv

names = {}

def calculate_word_value(word):
	return names[word] * sum(map(calculate_letter_value, word))
	
def calculate_letter_value(letter):
	return ord(letter) - 64

def create_names(filename):
	with open(filename, "r") as name_file:
		reader = csv.reader(name_file, delimiter=",")
		x = 1
		for row in reader:
			row.sort()
			for name in row:
				names[name] = x
				x += 1
			
def names_value_sum(filename):
	create_names(filename)
	return sum(map(calculate_word_value, names))
	
print names_value_sum("../files/names.txt")