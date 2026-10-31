def set_intersection(A, B):
    n = len(A)
    m = len(B)

    A = sorted(A)
    B = sorted(B)

    C = []
    i = 0
    j = 0

    while i < n and j < m:
        if A[i] == B[j]:
            C.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1

    return C