from stack import Stack
def evaluatePostfixExp(exp):
    '''
    Objective: To evaluate postfix expression 
    Input Parameter: exp - string (postfix expression)
    Return Value: result - integer

    Limitation: operands are single digit integers, 
                Only binary arithmetic operands are allowed
    '''
    stk = Stack()
    operations = ['+','-','*','/']
    for symbol in exp:
        if symbol in operations:
            operand2 = stk.pop()
            operand1 = stk.pop()
            result = str(eval(operand1 + symbol + operand2))
            stk.push(result)
        else:
            stk.push(symbol)
    result = int(stk.pop())
    return result
def main():
    '''
    Objective: To evaluate postfix expression entered by the user 
    Input Parameter: None
    Return Value: None
    Assumption: Input expression is correctly formed
    '''
    exp = input('Enter a postfix expression - use single digit numbers only: ')
    result = evaluatePostfixExp(exp)
    print(result)

if __name__=='__main__':
    main()