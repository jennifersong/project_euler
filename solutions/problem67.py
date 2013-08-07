import csv

triangle = []
routes = {}

def int_strip_leading_zeros(num):
	if num[0:1] == "0":
		return int(num[1])
	else:
		return int(num)

def create_triangle():
	with open("../files/triangle100.txt", "r") as triangle_file:
		reader = csv.reader(triangle_file, delimiter=" ")
		for row in reader:
			triangle.append(map(int_strip_leading_zeros, row))
	
def triangle_routes(x, y):
	if y == 0:		# First row, only one solution
		routes[(y, x)] = triangle[y][x]
	elif x == 0:	# Left side of triangle
		routes[(y, x)] = routes[(y-1, x)] + triangle[y][x]
	elif x == y:	# Right side of triangle
		routes[(y, x)] = routes[(y-1, x-1)] + triangle[y][x]
	else:
		routes[(y, x)] = max(routes[(y-1, x)], routes[(y-1, x-1)]) + triangle[y][x]

def max_route(y):
	create_triangle()
	for i in range(0, y):
		for j in range(i+1):	# x coordinate can only be <= y
			triangle_routes(j, i)
	return max(routes.itervalues())
	
print max_route(100)