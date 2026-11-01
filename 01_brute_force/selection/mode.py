def mode(A):
    n = len(A)
    if n == 0:
        return None

    mode_qnt = 0
    mode = A[0]
    count = 1

    for i in range(n):
        count = 1
        for j in range (i+1, n):
            if A[i] == A[j]:
                count += 1   

        if count > mode_qnt:
            mode_qnt = count
            mode = A[i]

    return mode