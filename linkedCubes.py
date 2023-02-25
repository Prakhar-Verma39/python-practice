from node import Node
def main():
    '''
    Objective: To create a linked list comprising of four nodes 
    Input Parameter: None
    Return Value: None
    '''
    start, finish = 2, 5
    lst = Node(1)
    current = lst
    for i in range(start, finish):
        current.next = Node(i**3)
        current = current.next

if __name__=='__main__':
    main()