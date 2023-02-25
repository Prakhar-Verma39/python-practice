from linkedList import LinkedList
def main():
    '''
    Objective: To carry out linked list operations based on user inputs
    Input Parameter: None
    Return Value: None
    '''
    lst = LinkedList()
    while 1: 
        choice = int(input('1: Insert in Beginning \n 2: Delete from Beginning \n 3: Quit\n'))
        if choice == 1:
            value = eval(input('Enter value to be inserted: '))
            lst.insertBegin(value)
        elif choice == 2:
            value = lst.delBegin()
            print('Value Deleted!!', value)
        elif choice == 3:
            break

if __name__=='__main__':
    main()