from queue import Queue
def main():
    '''
    Objective: To provide queue functionality
    Input Parameter: None
    Return Value: None
    '''
    while 1:
        print('Choose an option \n')
        print('1: Create queue')
        print('2: Delete queue')
        print('3: Enqueue')
        print('4: Dequeue')
        print('5: Print Queue Data')
        print('6: Front elements')
        print('7: No. of elements')
        choice = int(input('Enter Choice: '))
        if choice == 1:
            q = Queue()
            print('Queue Created')
        elif choice == 2:
            del q
            print('Queue Deleted')
        elif choice == 3:
            element = int(input('Enter element to be inserted: '))
            q.enqueue(element)
        elif choice == 4:
            print('Element deleted:', q.dequeue())
        elif choice == 5:
            print(q)
        elif choice == 6:
            print('Front element',q.front())
        elif choice == 7:
            print('No. of elements', q.size())
        proceed = input('enter y if you wish to continue: ')
        if proceed != 'y' and proceed != 'Y':
            break

if __name__=='__main__':
    main()

