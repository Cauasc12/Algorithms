def lomuto_partition(array, l, r):
    p = array[l]
    s = l

    for i in range(l+1, r+1):
        if array[i] < p:
            s += 1
            array[i], array[s] = array[s], array[i]
    array[s], array[l] = array[l], array[s]
    return s

def quickselect(array, l, r, k):
    """Select an order statistic by recursive partitioning.
    
    Preconditions:
    For a whole-list query use l = 0, r = len(array) - 1, and
    1 <= k <= len(array). Input must be a nonempty mutable list of
    mutually comparable values. Duplicates are allowed.
    
    Result:
    Return the kth smallest value; partitioning modifies the input.
    For a restricted interval, k - 1 is an absolute array index.
    """
    s = lomuto_partition(array, l, r)

    if s == k-1:
        return array[s]
    elif s > k-1:
        return quickselect(array, l, s-1, k)
    else:
        return quickselect(array, s+1, r, k)