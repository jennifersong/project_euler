n = 28433
for x in xrange(7830457):
    n = (n * 2) % 10000000000
print str(n+1)[-10:]