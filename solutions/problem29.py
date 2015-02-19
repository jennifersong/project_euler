generated = {}

for a in xrange(2, 101):
    for b in xrange(2, 101):
        current = pow(a, b)
        if current not in generated:
            generated[current] = True
            
print len(generated.keys())