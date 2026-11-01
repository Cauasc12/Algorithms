def mode(A):
    A = sorted(A)
    n = len(A)
    if n == 0:
        return None

    mode_qnt = 0
    mode = A[0]
    count = 1
    
    for i in range(n-1):
        if A[i] == A[i+1]:
            count += 1
        else:
            if count > mode_qnt:
                mode_qnt = count
                mode = A[i]
            count = 1

    if count > mode_qnt:
        mode_qnt = count
        mode = A[n-1]

    return mode