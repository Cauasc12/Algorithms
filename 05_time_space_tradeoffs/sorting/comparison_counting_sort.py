def comparison_counting_sort(A):
    n = len(A)
    count = [0] * n
    S = [0] * n
    
    for i in range(n-1):
        for j in range(i+1, n):
            if A[i] < A[j]:
                count[j] += 1
            else:
                count[i] +=1

    for i in range(n):
        S[count[i]] = A[i]

    return S