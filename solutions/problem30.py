fifth_powers = []
for num in xrange(2, 1000000):
    fifth_power_sum = sum([pow(int(d), 5) for d in list(str(num))])
    if fifth_power_sum == num:
        fifth_powers.append(num)
print sum(fifth_powers)