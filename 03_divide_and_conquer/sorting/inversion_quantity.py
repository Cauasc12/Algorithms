def merge_and_count(A, temp, left, right):
    mid = (left + right) // 2

    i = left
    j = mid+1
    k = left
    inversions = 0

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            temp[k] = A[i]
            i += 1
        else:
            temp[k] = A[j]
            j += 1
            inversions += mid - i + 1
        k += 1

    while i <= mid:
        temp[k] = A[i]
        i += 1
        k += 1
    while j <= right:
        temp[k] = A[j]
        j += 1
        k += 1

    for i in range(left, right+1):
        A[i] = temp[i]

    return inversions

def count_inversions(array, temp, left, right):
    inversions = 0

    if left < right:
        mid = (left + right) // 2

        inversions += count_inversions(array, temp, left, mid)
        inversions += count_inversions(array, temp, mid+1, right)
        inversions += merge_and_count(array, temp, left, right)

    return inversions