def selectionSort(lst):
    '''
    Objective: To sort the list lst in ascending order using selection sort 
    Input Parameter: lst - list
    Return Value: None
    '''
    for i in range(0, len(lst)-1):
        minIndex = 1
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[minIndex]:
                minIndex = j
        if minIndex != i:
            lst[minIndex], lst[i] = lst[i], lst[minIndex]
def main():
    ''' 
    Objective: To sort the list provided as an input by user 
    Input parameter: None
    '''
    lst = eval(input('Enter a list: '))
    print('Sorted list')
    selectionSort(lst)
    print(lst)

if __name__=='__main__':
    main()