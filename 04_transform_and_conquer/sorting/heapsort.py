def heapify(H, n, i=None):
    if i is None:
        for start in range(n//2 -1, -1, -1):
            heapify(H, n, start)
        return
    
    k = i
    v = H[k]
    heap = False

    while not heap and 2*k + 1 < n:
        j = 2*k + 1
        if j+1 < n and H[j] < H[j+1]:
            j += 1
        if v >= H[j]:
            heap = True
        else:
            H[k] = H[j]
            k = j
    H[k] = v
    
    return H

def heapsort(array):
    n = len(array)
    heapify(array, n)

    for i in range(n -1, 0, -1):
        array[0], array[n] = array[n], array[0]
        heapify(array, i, 0)
    
    return array