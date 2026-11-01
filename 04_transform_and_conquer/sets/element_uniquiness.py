def element_uniquiness(A):
    n = len(A)
    A = sorted(A, 0, n-1)

    for i in range(n-1):
        if A[i] == A[i+1]:
            return False

    return True