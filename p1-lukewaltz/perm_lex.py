
def string_to_list(str1):  # helper functions
    return_lst = []
    for i in range(len(str1)):
        return_lst.append(str1[i])
    return return_lst


def list_to_string(lst2):  # helper functions
    str2 = ""
    for char2 in lst2:
        str2 += char2
    return str2


def perm_gen_lex(str_in):
    resultList = []
    if len(str_in) == 1:  # base case 1
        return string_to_list(str_in)
    if not str_in:  # base case 2
        return []
    for i in range(len(str_in)):  # For each index in the input string
        # Form a simpler string by removing the first character from the input string
        lst_in = string_to_list(str_in)
        charPulled = lst_in.pop(i)  # char pulled out
        narrowLst2 = lst_in[i:]  # remaining string after the letter that was removed
        narrowLst1 = lst_in[:i]  # remaining string before the letter that was removed
        narrowLst = narrowLst1 + narrowLst2  # remaining list to get manipulated
        narrowStr = list_to_string(narrowLst)  # convert list to string, so it can be used in recursion
        nextStr = perm_gen_lex(narrowStr)  # recursive call
        for j in range(len(nextStr)):
            perm = charPulled + nextStr[j]
            resultList.append(perm)
    return resultList

