from decimal import *
getcontext().prec = 200     # set precision very high to accommodate for premature rounding

current, total = 0, 0
while current <= 100:
    square_root = Decimal(current).sqrt()
    str_square_root = str(square_root)
    if '.' in str_square_root:
        str_square_root = str_square_root[:101]     # we only want the first 100 decimal digits
        digital_sum = sum((int(x) for x in str_square_root if x.isdigit()))
        total += digital_sum
    current += 1
print total