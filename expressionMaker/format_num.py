from gcd import reduce_factor

def format_num(numerator, denominator):
    numerator = int(numerator)
    denominator = int(denominator)
    remainder = numerator % denominator
    if remainder == 0:
        return str(numerator//denominator)
    elif numerator > denominator:
        return str(numerator//denominator) + '’' + reduce_factor(str(remainder) + '/' + str(denominator))
    elif numerator < denominator:
        return reduce_factor(str(remainder) + '/' + str(denominator))
