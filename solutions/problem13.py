with open('../files/50digitnumbers.txt') as file:
    sum = 0
    for line in file:
        sum += int(line)
    print sum