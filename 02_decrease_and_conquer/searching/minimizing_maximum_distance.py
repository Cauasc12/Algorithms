def minimizing_maximum_distance(array):
    """Choose an input element minimizing its maximum distance to the others.
    
    Preconditions:
    Input must be a nonempty numeric sequence sorted in nondecreasing
    order. Arithmetic must preserve the midpoint comparisons.
    
    Result:
    Return a zero-based optimal index; any optimal index is valid on ties.
    """
    n = len(array)
    target = (array[0] + array[n-1]) / 2
    begin = 0
    end = n-1

    while begin <= end:
        mid = (begin + end) // 2
        if array[mid] == target:
            return mid
        if array[mid] < target:
            begin = mid+1
        elif array[mid] > target:
            end = mid-1

    if begin >= n:
        return end
    if end < 0:
        return begin
    
    if abs(array[begin] - target) < abs(array[end] - target):
        return begin
    
    return end
