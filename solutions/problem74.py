facts = {0: 1}

def factorial(n):
    if n not in facts:
        facts[n] = n * facts[n-1]
    return facts[n]
    
def sum_factorial(n):
    chains = {}
    while n not in chains:
        temp = n
        total = 0
        while n:
            digit = n % 10
            total += factorial(digit)
            n = (n - digit) / 10
        chains[temp] = total
        n = total
    return chains
    
# note: runs in 40-41 seconds
count = 0        
for x in xrange(10):
    factorial(x)
for x in xrange(100000):
    chain = sum_factorial(x)
    if len(chain.keys()) == 60:
        count += 1
print count