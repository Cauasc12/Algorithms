def distribution_counting_sort(A, l, u):
    n = len(A)

    S = [0] * n
    D = [0] * (u-l+1)
    
    for i in range(n):
        D[A[i]-l] += 1
    
    for i in range(1, u-l+1):
        D[i] += D[i-1]

    for i in range(n-1, -1, -1):
        j = A[i] - l
        S[D[j] - 1] = A[i]
        D[j] -= 1

    return S