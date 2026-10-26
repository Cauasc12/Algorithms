#sorted array with n-1 elements
def missing_number(array):
    """Find the single missing integer from the range 1 through N.
    
    Preconditions:
    Input must contain all other integers in strictly increasing order.
    An empty input represents N = 1 and returns 1.
    
    Result:
    Return the missing value, not its index.
    """
    n = len(array)
    l = 0
    r = n-1

    while l <= r:
        mid = (l + r) // 2
        if array[mid] == mid+1:
            l = mid + 1
        else:
            r = mid - 1

    return l + 1