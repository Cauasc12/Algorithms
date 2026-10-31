def merge(A, B, C):
    i = 0
    j = 0
    k = 0

    b = len(B)
    c = len(C)

    while i < b and j < c:
        if(B[i] <= C[j]):
            A[k] = B[i]
            i += 1
            k += 1
        else:
            A[k] = C[j]
            j += 1
            k += 1
   
    while j < c:
        A[k] = C[j]
        j += 1
        k += 1
    while i < b:
        A[k] = B[i]
        i += 1
        k += 1

def mergesort(A):
    n = len(A)
    mid = n //2

    if(n > 1):
        B = mergesort(A[:mid])
        C = mergesort(A[mid:])

        merge(A, B, C)

    return A