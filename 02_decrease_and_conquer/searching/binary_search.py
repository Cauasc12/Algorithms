def binary_search(array, target):
    """Find a target in a sequence sorted in nondecreasing order.
    
    Preconditions:
    Elements and target must be mutually comparable; duplicates are allowed.
    
    Result:
    Return a zero-based matching index, or -1 when absent.
    """
    n = len(array)
    l = 0
    r = n-1

    while l <= r:
        mid = (r+l) // 2
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            r = mid - 1
        else:
            l = mid + 1

    return -1