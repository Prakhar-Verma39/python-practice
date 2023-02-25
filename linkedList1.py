from node import Node
def main():
    '''
    Objective: To create a linked list comprising of three nodes
    Input Parameter: None
    Return Value: None
    '''
    lst = Node(20)
    lst.next = Node(15)
    lst.next.next = Node(25)
    print('lst', lst)
    print('lst.data', lst.data)
    print('lst.next', lst.next)
    print('lst.next.data',lst.next.data)
    print('lst.next.next',lst.next.next)
    print('lst.next.next.data', lst.next.next.data)

if __name__=='__main__':
    main()