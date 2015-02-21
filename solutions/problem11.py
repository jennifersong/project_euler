def can_go_down(coords):
    y, x = coords
    return y < 17
    
def can_go_right(coords):
    y, x = coords
    return x < 17
    
def can_go_right_diagonal(coords):
    y, x = coords
    return can_go_down(coords) and can_go_right(coords)
    
def can_go_up(coords):
    y, x = coords
    return y > 2

def can_go_left_diagonal(coords):
    y, x = coords
    return can_go_right(coords) and can_go_up(coords)
    
def get_max_product_from_point(coords):
    y, x = coords
    down = grid[y][x] * grid[y+1][x] * grid[y+2][x] * grid[y+3][x] if can_go_down(coords) else 0
    right = grid[y][x] * grid[y][x+1] * grid[y][x+2] * grid[y][x+3] if can_go_right(coords) else 0
    right_diag = grid[y][x] * grid[y+1][x+1] * grid[y+2][x+2] * grid[y+3][x+3] if can_go_right_diagonal(coords) else 0
    left_diag = grid[y][x] * grid[y-1][x+1] * grid[y-2][x+2] * grid[y-3][x+3] if can_go_left_diagonal(coords) else 0
    return max(down, right, right_diag, left_diag)

grid = []
values = {}
with open('../files/20x20grid.txt') as file:
    for line in file:
        grid.append(map(int, line.split()))

for x in xrange(20):
    for y in xrange(20):
        coords = (y, x)
        values[coords] = get_max_product_from_point(coords)
print max(values.itervalues())