def selection_sort(array):
    """Sort a mutable list in place in nondecreasing order.
    
    Preconditions:
    Elements must be mutually comparable. Empty lists and duplicates are allowed.
    
    Result:
    Return None; the input list is modified.
    """
    n = len(array)
    
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if(array[min_index] > array[j]):
                min_index = j
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]