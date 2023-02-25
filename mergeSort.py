def merge(lst1 , lst2):
    '''
    Objective: To merge two sorted lists into a single sorted list 
    Input Parameter: lst1, lst2 - list
    Return Value: sorted list
    '''
    sortedLst = []
    while len(lst1) != 0 and len(lst2) != 0:
        if lst1[0] < lst2[0]:
            sortedLst.append(lst1[0])
            lst1.remove(lst1[0])
        else:
            sortedLst.append(lst2[0])
            lst2.remove(lst2[0])
    if len(lst1) == 0:
        sortedLst += lst2
    else:
        sortedLst += lst1
    return sortedLst

def mergeSort(lst):
    '''
    Objective: To sort the list in ascending order using merge sort
    Input Parameter: lst - list
    Return Value: sorted list
    '''
    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        mid = len(lst)//2
        lst1 = mergeSort(lst[:mid])
        lst2 = mergeSort(lst[mid:])
        return merge(lst1,lst2)
        
def main():
    lst = eval(input('Enter a list: '))
    print('Sorted list: ')
    print(mergeSort(lst))

if __name__=='__main__':
    main()