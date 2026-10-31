def is_sum(array, s):
    n = len(array)
    array = sorted(array)

    i = 0
    j = n - 1

    while i < j:
        sum = array[i] + array[j]

        if sum == s:
            return True
        elif sum < s:
            i += 1
        else:
            j -= 1

    return False