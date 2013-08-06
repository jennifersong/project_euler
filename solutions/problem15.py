paths = {}

def lattice_paths(x, y):
	if x == 0 or y == 0:
		paths[(x, y)] = 1
	elif (x, y) not in paths:
		paths[(x, y)] = paths[(x, y-1)] + paths[(x-1, y)]

def num_paths(x, y):
	for i in range(x+1):		# Coordinates start from (0, 0) so an x by y grid has x+1 rows
		for j in range(y+1):
			lattice_paths(i, j)
	return paths[(x, y)]

print num_paths(20, 20)