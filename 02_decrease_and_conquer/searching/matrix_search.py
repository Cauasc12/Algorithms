def matrix_search(matrix, target):
    """Find a target in a square matrix, as required by the exercise.
    
    Preconditions:
    Input must be an n-by-n matrix with every row and column sorted in
    nondecreasing order. Values and target must be mutually comparable.
    
    Result:
    Return a zero-based (row, column), or -1 when absent; [] returns -1.
    """
    n = len(matrix)

    i = 0
    j = n-1

    while  i < n and j >= 0:
        if matrix[i][j] == target:
            return (i, j)
        if matrix[i][j] < target:
            i += 1
        else:
            j -= 1

    return -1