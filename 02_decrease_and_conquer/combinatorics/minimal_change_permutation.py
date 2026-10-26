def minimal_change_permutation(number):

    """Generate permutations by alternating insertion positions.
    
    Preconditions:
    Input must be a nonempty list of distinct elements.
    
    Result:
    Return all permutations as lists; consecutive permutations differ
    by one adjacent swap.
    """
    n = len(number)
    if(n == 1):
        return [[number[0]]]
    last_element = number[n-1]

    previous_permutation = minimal_change_permutation(number[0:n-1])
    permuations = []

    for i in range(len(previous_permutation)):
        current_permutation = previous_permutation[i]

        if i % 2 == 0:
            for pos in range(len(current_permutation), -1, -1):
                new_permutation = current_permutation[:pos] + [last_element] + current_permutation[pos:]
                permuations.append(new_permutation)
        else:
            for pos in range(len(current_permutation) + 1):
                new_permutation = current_permutation[:pos] + [last_element] + current_permutation[pos:]
                permuations.append(new_permutation)

    return permuations