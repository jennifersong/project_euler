palindromes = []

def convert_to_binary(num):
    return bin(num)[2:]

for num in xrange(1000000):
    str_num = str(num)
    if str_num == str_num[::-1]:
        binary = convert_to_binary(num)
        if binary == binary[::-1]:
            palindromes.append(num)
print sum(palindromes)