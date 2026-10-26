def flip(array, k):
    l = 0
    r = k
    while l < r:
        array[l], array[r] = array[r], array[l]
        l += 1
        r -= 1

def pancake_sort(pancakes):
    """Sort a mutable list using prefix reversals.
    
    Preconditions:
    Elements must be mutually comparable. Empty lists and duplicates are allowed.
    
    Result:
    Return the input list, sorted in place in nondecreasing order.
    """
    for i in range(len(pancakes), 1, -1):

        bigger_index = 0
        for j in range(i):
            if pancakes[j] > pancakes[bigger_index]:
                bigger_index = j

        if bigger_index != i-1:

            if bigger_index != 0:
                flip(pancakes, bigger_index)
        
            flip(pancakes, i-1)

    return pancakes