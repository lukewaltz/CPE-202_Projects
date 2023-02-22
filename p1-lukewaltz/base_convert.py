# int, int -> string
# Given integer num and base b, converts num to a string representation in base b
def convert(num, b):
    resultStr = ''
    # integer division for input base ten number (input // desired base)
    try:
        nextInput = num // b
        remainder = num % b
    except TypeError as TE:
        return num
    if b < 0:
        return False
    if b == 10:
        return str(num)  # base cases
    if num == 0:
        return resultStr  # base cases
    if remainder == 0:
        if nextInput < 0:
            return str(nextInput)
        else:
            return str(convert(nextInput, b)) + str(remainder) + resultStr

    if remainder == 10:
        remainder = 'A'
    if remainder == 11:
        remainder = 'B'
    if remainder == 12:
        remainder = 'C'
    if remainder == 13:
        remainder = 'D'
    if remainder == 14:
        remainder = 'E'
    if remainder == 15:
        remainder = 'F'

    result = str(convert(nextInput, b)) + str(remainder)
    resultStr = str(result) + str(resultStr)

    if nextInput == 0:
        return resultStr

    return resultStr

