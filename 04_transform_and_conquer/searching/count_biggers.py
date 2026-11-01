def count_biggers(heap, v, i=1):
    n = len(heap)
    if i >= n or heap[i] <= v:
        return 0

    return 1 + count_biggers(heap, v, 2*i+1) + count_biggers(heap, v, 2*i+2)