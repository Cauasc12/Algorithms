def lexicographic_permutation(input):

    """Generate permutations in lexicographic order.
    
    Preconditions:
    Input is a nonnegative integer n (representing 1 through n), or
    a list of mutually comparable values. To enumerate all permutations,
    the list must initially be sorted in nondecreasing order.
    
    Result:
    Return permutations starting at the supplied arrangement. Duplicate
    values are allowed; an empty input returns [[]].
    """
    if isinstance(input, int):
        base = [i+1 for i in range(input)]
    else:
        base = list(input)

    n = len(base)
    permutations = [base.copy()]

    while True:
        i = n-2
        while i >= 0 and base[i] >= base[i+1]:
              i -= 1

        if i < 0:
            break

        j = n-1
        while base[j] <= base[i]:
            j -= 1
        base[i], base[j] = base[j], base[i]
        
        base[i+1:] = base[i+1:][::-1]
        permutations.append(base.copy())

    return permutations