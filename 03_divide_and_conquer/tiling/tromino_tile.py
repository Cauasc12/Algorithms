def tromino_tile(board, missing):

    n = len(board)
    mx, my = missing
    board[mx][my] = -1

    counter_tromino = 1

    def tile(n, top_left, current_role):
        nonlocal counter_tromino        

        if n == 2:
            id = counter_tromino
            counter_tromino += 1

            r_top, c_top = top_left
            for r in range(r_top, r_top+2):
                for c in range(c_top, c_top+2):
                    if (r, c) != current_role:
                        board[r][c] = id
            return

        half = n // 2
        r_top, c_top = top_left
        hr, hc = current_role

        id = counter_tromino
        counter_tromino += 1

        row_up = r_top + half
        row_down = r_top + half - 1
        column_right = c_top + half
        column_left = c_top + half - 1

        #1 quarter
        if hr <= row_down and hc <= column_left :
            tile(half, (r_top, c_top), current_role)
        else:
            board[row_down][column_left] = id
            tile(half, (r_top, c_top), (row_down, column_left))

        #2 quarter
        if hr <= row_down and hc >= column_right:
            tile(half, (r_top, c_top + half), current_role)
        else:
            board[row_down][column_right] = id
            tile(half, (r_top, c_top + half), (row_down, column_right))

        #3 quarter
        if hr >= row_up and hc <= column_left:
            tile(half, (r_top + half, c_top) , current_role)
        else:
            board[row_up][column_left] = id
            tile(half, (r_top + half, c_top), (row_up, column_left))
        
        #4 quarter
        if hr >= row_up and hc >= column_right:
            tile(half, (r_top + half, c_top + half) , current_role)
        else:
            board[row_up][column_right] = id
            tile(half, (r_top + half, c_top + half), (row_up, column_right))

    tile(n, (0,0), missing)
    return board