numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

special_numbers = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

def split_number(num):
    subnumbers = []
    if num >= 1000:
        subnumbers.append(num / 1000)
        subnumbers.append(1000)
        num -= (num / 1000 * 1000)
    if num >= 100:
        subnumbers.append(num / 100)
        subnumbers.append(100)
        num -= (num / 100 * 100)
    if num in special_numbers:
        subnumbers.append(num)
        num -= num
    if num > 10:
        subnumbers.append(num / 10 * 10)
        num -= (num / 10 * 10)
    if num > 0:
        subnumbers.append(num)
    return subnumbers

lengths = 0
for num in xrange(1, 1001):
    if num in special_numbers:
        lengths += len(special_numbers[num])
    else:
        deconstructed = split_number(num)
        if len(deconstructed) >= 3:
            lengths += 3 # for "and"
        for number in deconstructed:
            lengths += len(numbers[number])
print lengths