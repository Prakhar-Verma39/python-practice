from stack import Stack 

def postfix(exp):
    '''
    Objective: To convert infix expression to postfix
    Input Parameter: exp - string (infix expression)
    Return Value: result - string (postfix expression)
    '''
    # precedence: dictionary to store operator: precedence pairs
    precedence = {'+':1,'-':1, '*':2, '/':2}
    operand = '0123456789' #string of valid operands

    result = ''
    stk = Stack()
    for symbol in exp:
        if symbol == '(':
            stk.push(symbol)
        elif symbol == ')':
            val = stk.pop()
            while val != '(':
                result += val
                val = stk.pop()
        elif symbol in operand:
            result += symbol
        elif symbol in precedence:
            if not(stk.isEmpty()):
                stkTop = stk.top()
            while not(stk.isEmpty()) and stkTop != '(' and precedence[stkTop] >= precedence[symbol]:
                result += stkTop
                stk.pop()
                if not(stk.isEmpty()):
                    stkTop = stk.top()
            stk.push(symbol)
    while not(stk.isEmpty()):
        result += stk.pop()
    return result
def main():
    '''
    Objective: To convert infix expression provided by user to postfix expressions
    Input Parameter: None
    Return Value: None
    '''
    '''
    Assumption: Input expression is correctly formed
    '''
    exp = input('Enter the expression in infix notation:  ')
    exp = postfix(exp)
    print(exp)

if __name__=='__main__':
    main()    