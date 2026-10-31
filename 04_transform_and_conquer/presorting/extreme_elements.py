def extreme_elements(array):
    array = sorted(array)

    smallest = array[0]
    largest = array[-1]

    return smallest, largest