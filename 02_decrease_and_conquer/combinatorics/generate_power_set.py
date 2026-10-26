def generate_power_set(elements):
    """Generate every subset of a list of distinct elements.
    
    Preconditions:
    Input is a list with no duplicate elements; the empty list is allowed.
    
    Result:
    Return subsets as lists, including the empty subset.
    """
    n = len(elements)
    if(n == 0):
        return [[   ]]

    previous = generate_power_set(elements[:n-1])
    result = []

    for e in previous:
        result.append(e)
        new = e + [elements[n-1]]
        result.append(new)

    return result