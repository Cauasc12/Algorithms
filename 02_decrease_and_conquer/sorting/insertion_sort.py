def insertion_sort(array):
    """Sort a mutable list in place in nondecreasing order.
    
    Preconditions:
    Elements must be mutually comparable. Empty lists and duplicates are allowed.
    
    Result:
    Return None; the input list is modified.
    """
    n = len(array)

    for i in range(1 , n):
        value = array[i]
        j = i - 1

        while j >= 0 and array[j] > value:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = value
