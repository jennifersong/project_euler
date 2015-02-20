def digital_sum(n):
    return int(reduce(lambda x, y: int(x) + int(y), str(n)))
    
max_digital_sum = 0
for a in xrange(100):
    for b in xrange(100):
        max_digital_sum = max(digital_sum(pow(a, b)), max_digital_sum)
print max_digital_sum