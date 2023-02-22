from stack_array import Stack


# You do not need to change this class
class PostfixFormatException(Exception):
    pass


def precedence(op):
    '''Helper function that is called when the precedence of an operator is needed.'''
    if op == '<<' or op == '>>':
        return 4
    if op == '**':
        return 3
    if op == '*' or op == '/':
        return 2
    if op == '+' or op == '-':
        return 1


def postfix_eval(input_str):
    '''Evaluates a postfix expression
    Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ** >> << or numbers.
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed
    DO NOT USE PYTHON'S EVAL FUNCTION!!!'''
    if input_str is None:
        return None
    if input_str == "":
        raise PostfixFormatException("Empty input")
    input_lst = input_str.split()  # use split() method to separate tokens from string
    operand_stack = Stack(30)
    for item in input_lst:
        if item == '+' or item == '-' or item == '*' or item == '/' or item == '**' or item == '>>' or item == '<<':
            if operand_stack.num_items >= 2:  # if operator pop both and choose what operator to use
                v1 = operand_stack.pop()
                v2 = operand_stack.pop()

                if item == '+':  # if token == operator
                    result = float(v2) + float(v1)
                    operand_stack.push(result)

                elif item == '-':
                    result = float(v2) - float(v1)
                    operand_stack.push(result)

                elif item == '**':
                    result = float(v2) ** float(v1)
                    operand_stack.push(result)

                elif item == '*':
                    result = float(v2) * float(v1)
                    operand_stack.push(result)

                elif item == '/':
                    if float(v1) == 0:
                        raise ValueError
                    result = float(v2) / float(v1)
                    operand_stack.push(result)

                elif item == '>>':  # bit shift
                    try:
                        cast = int(v1)
                        cast2 = int(v2)
                        result = int(v2) >> int(v1)
                        operand_stack.push(result)
                    except ValueError:
                        raise PostfixFormatException("Illegal bit shift operand")
                elif item == '<<':
                    try:
                        cast = int(v1)
                        cast2 = int(v2)
                        result = int(v2) << int(v1)
                        operand_stack.push(result)
                    except ValueError:
                        raise PostfixFormatException("Illegal bit shift operand")
            else:
                # not enough operands to perform computation
                raise PostfixFormatException("Insufficient operands")
        else:
            try:  # if token == int
                cast = float(item)
                operand_stack.push(item)
            except ValueError:
                raise PostfixFormatException("Invalid token")

    if operand_stack.num_items > 1:  # return value once for loop ends
        raise PostfixFormatException("Too many operands")
    result = float(operand_stack.pop())
    return result


def infix_to_postfix(input_str):
    '''Converts an infix expression to an equivalent postfix expression
    Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << parentheses ( ) or numbers
    Returns a String containing a postfix expression '''
    if input_str is None:
        return None
    if input_str == "":
        raise PostfixFormatException("Empty input")
    input_lst = input_str.split()
    RPN_lst = []
    operator_stack = Stack(30)
    for item in input_lst:

        if item == '(':
            operator_stack.push(item)  # if open paren --> push to operator stack

        elif item == ')':
            while operator_stack.is_empty() is False and operator_stack.peek() != '(':
                v = operator_stack.pop()  # if closed paren --> pop everything back to open paren
                RPN_lst.append(v)
            operator_stack.pop()  # pop but don't append the paren

        elif item == '+' or item == '-' or item == '*' or item == '/' or item == '**' or item == '<<' or item == '>>':
            # insert special case for right associative '**'
            if item == '**':  # right ass
                while operator_stack.num_items != 0 and operator_stack.peek() != '(' and \
                        precedence(item) < precedence(operator_stack.peek()):
                    v = operator_stack.pop()
                    RPN_lst.append(v)
            else:
                while operator_stack.num_items != 0 and operator_stack.peek() != '(' and \
                        precedence(item) <= precedence(operator_stack.peek()):
                    v = operator_stack.pop()  # if operator --> pop & add to RPN until:
                    RPN_lst.append(v)  # the stack is empty OR operator_stack.peek == '('
            operator_stack.push(item)

        else:
            RPN_lst.append(item)  # if number --> output to RPN expression

    while operator_stack.num_items != 0:  # empty stack to RPN at end of loop
        v = operator_stack.pop()  # pop & add all to RPN
        RPN_lst.append(v)
    RPN_str = ' '.join(RPN_lst)
    return RPN_str  # return RPN


def prefix_to_postfix(input_str):
    '''Converts a prefix expression to an equivalent postfix expression
    Input argument:  a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ** >> << or numbers
    Returns a String containing a postfix expression (tokens are space separated)'''
    #  reverse the PN expression
    if input_str is None:
        return None
    if input_str == "":
        raise PostfixFormatException("Empty input")
    input_lst = input_str.split()
    rev_lst = input_lst[-1::-1]
    operand_stack = Stack(30)
    #  for item in reversed list:
    for item in rev_lst:

        #  if item == operator
        if item == '+' or item == '-' or item == '*' or item == '/' or item == '**':
            op1 = operand_stack.pop()
            op2 = operand_stack.pop()
            push_str = op1 + ' ' + op2 + ' ' + item
            operand_stack.push(push_str)
        #  if item == operand push onto operand stack
        else:
            operand_stack.push(item)

        #  repeat all until input string is over
    return_lst = operand_stack.pop()
    return return_lst  # return the only remaining str in the stack
