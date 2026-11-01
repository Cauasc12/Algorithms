def number_placement(numbers, inequalities):
    n = len(numbers)
    m = len(inequalities)
    numbers.sort()

    i = 0
    j = n-1
    k = 0 

    result = []

    while k < m:
        if inequalities[k] == '<':
            result.append(numbers[i])
            i += 1
        elif inequalities[k] == '>':
            result.append(numbers[j])
            j -= 1
        k += 1

    result.append(numbers[i])

    return result