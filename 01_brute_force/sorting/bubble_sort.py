def bubble_sort(array):
    """Sort a mutable list in place in nondecreasing order.
    
    Preconditions:
    Elements must be mutually comparable. Empty lists and duplicates are allowed.
    
    Result:
    Return None; the input list is modified.
    """
    n = len(array)
    
    for i in range(n):
        change = False
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j+1], array[j] = array[j], array[j+1]
                change = True
        if change == False:
            break