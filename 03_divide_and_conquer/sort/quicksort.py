def HoarePartition(A, l, r):
    p = A[(l + r) // 2]
    i = l
    j = r

    while i < j:
        while A[i] < p:
            i += 1
            
        while A[j] > r:
            j -= 1
            
        A[i], A[j] = A[j], A[i]

    return i

def quicksort(A, l, r):
    if l < r:
        s = HoarePartition(A, l, r)
        quicksort(A, l, s)
        quicksort(A, s+1, r)

    return A
