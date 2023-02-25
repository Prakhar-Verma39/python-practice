from stack import Stack
def main():
    '''
    Objective: To provide stack functionality
    Input Parameter: None
    Return Value: None
    '''
    while 1:
        print('Choose an option \n')
        print('1: Create stack')
        print('2: Delete stack')
        print('3: Push')
        print('4: Pop')
        print('5: Print Stack Data')
        print('6: Top elements')
        print('7: No. of elements')
        choice = int(input('Enter Choice: '))
        if choice == 1:
            stk = Stack()
            print('Stack Created')
        elif choice == 2:
            del stk
            print('Stack Deleted')
        elif choice == 3:
            element = int(input('Enter element to be inserted: '))
            stk.push(element)
        elif choice == 4:
            print('Element poped:', stk.pop())
        elif choice == 5:
            print(stk)
        elif choice == 6:
            print('Top element',stk.top())
        elif choice == 7:
            print('No. of elements', stk.size())
        proceed = input('enter y if you wish to continue: ')
        if proceed != 'y' and proceed != 'Y':
            break

if __name__=='__main__':
    main()