def string_matching(test, pattern):
    """Find the first occurrence of a pattern in a string.
    
    Preconditions:
    text (the parameter named test) and pattern are strings.
    
    Result:
    Return a zero-based index or -1 when absent. An empty pattern returns 0.
    """
    n = len(test)
    m = len(pattern)
    
    for i in range(n-m+1):
        j = 0
        while j < m and pattern[j] == test[i+j]:
            j += 1
        if j == m:
            return i
        
    return -1