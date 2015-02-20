import re

# Note: takes ~225 seconds to run
for num in xrange(10, 2000000000, 10):
    if re.match("^1\d{1}2\d{1}3\d{1}4\d{1}5\d{1}6\d{1}7\d{1}8\d{1}9\d{1}0$", str(pow(num, 2))):
        print num