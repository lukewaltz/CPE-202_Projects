# int -> boolean
# Given integer n, returns True or False based on reachabilty of goal
def bears(n):
    giveOption = 0
    try:  # accounts for non-int types with a throwaway variable
        isInt = n // 2
    except TypeError as TE:
        return False
    if n < 0:  # False if n is negative
        return False
    if n == 42:  # win condition
        return True
    if n % 5 == 0:  # n is divisible by 5
        giveOption = 42
        return bears(n - giveOption)  # recursive call
    if n % 3 == 0 or n % 4 == 0:  # n is divisible by 3 or 4
        int1 = n % 10  # takes last digit of n
        int2 = (n % 100)//10  # takes second to last digit of n
        giveOption = int1 * int2
        if giveOption != 0:
            return bears(n - giveOption)  # recursive call
    if n % 2 == 0:  # n is even
        giveOption = n // 2
        return bears(n - giveOption)  # recursive call
    return False  # fail





