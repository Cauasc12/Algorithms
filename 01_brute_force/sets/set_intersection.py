def set_intersection(A, B):
    n = len(A)
    m = len(B)

    C = []

    for i in range(n):
        for j in range(m):
            if A[i] == B[j]:
                C.append(A[i])
                break

    return C