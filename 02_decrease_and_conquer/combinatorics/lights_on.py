def lights_on(buttons):
    """Reach the all-on state using single-switch changes.
    
    Preconditions:
    buttons contains mutable [identifier, boolean_state] records.
    Each switch independently toggles only its own light.
    
    Result:
    Modify the states in place and return True once all are on.
    An empty input is already all-on and returns True.
    """
    n = len(buttons)

    all_on = True
    for b in buttons:
        if not b[1]:
            all_on = False
            break
    if all_on:
        return True

    total_steps = 2**n

    for i in range(1, total_steps):
        temp_i = i
        button = 1

        while temp_i % 2 == 0:
            temp_i //= 2
            button += 1

        btn_index = button - 1
        buttons[btn_index][1] = not buttons[btn_index][1]
        
        all_on = True
        for b in buttons:
            if not b[1]:
                all_on = False
                break
        if all_on:
            return True

    return False