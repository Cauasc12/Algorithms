#sorted array
def interpolation_search(array, target):
    """Find an integer target in a sorted integer sequence.
    
    Preconditions:
    The sequence must be in nondecreasing order; duplicates are allowed.
    
    Result:
    Return a zero-based matching index, or -1 when absent.
    """
    l = 0
    r = len(array)-1

    while l <= r and target >= array[l] and target <= array[r]:
        if array[l] == array[r]:
            if target == array[l]:
                return l
            else:
                return -1

        x = l + (((target - array[l]) * (r-l)) // (array[r] - array[l]))

        if array[x] == target:
            return x
        elif array[x] < target:
            l = x + 1
        else:
            r = x - 1

    return -1