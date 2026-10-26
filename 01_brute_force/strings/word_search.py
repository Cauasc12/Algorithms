def word_search(grid, array):
    """Find the first occurrence of each word on a circular grid.
    
    Preconditions:
    grid must be a nonempty rectangular grid with nonempty rows.
    array contains nonempty words. Search uses eight fixed directions;
    rows and columns wrap around, and cells may be reused after wrapping.
    
    Result:
    Return (word, (row, column), (dr, dc)) tuples with zero-based
    coordinates. Search starts in row-major order and uses the direction
    order in dir. Print a message for each absent word.
    """
    dir = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (1,-1), (-1,1), (-1,-1)]
    n = len(grid)
    m = len(grid[0])

    result = []

    for word in array:
        found = False

        for row in range(n):
            for column in range(m):
                for (dr, dc) in dir:
                    match = True
                    
                    for k in range(len(word)):
                        new_row = (row + k*dr) % n
                        new_column = (column + k*dc) % m

                        if grid[new_row][new_column] != word[k]:
                            match = False
                            break

                    if match:
                        found = True
                        result.append((word, (row,column), (dr,dc)))
                        break
                if found: break

            if found: break

        if not found:
            print(f"Word {word} was not found")
            
    return result
