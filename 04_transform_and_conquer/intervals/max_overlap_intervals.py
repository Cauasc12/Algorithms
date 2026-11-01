def max_overlap_intervals(intervals):
    starts = []
    ends = []
    for (a,b) in intervals:
        starts.append(a)
        ends.append(b)

    starts.sort
    ends.sort

    n = len(intervals)
    i = 0
    j = 0

    current_overlap = 0
    max_overlap = 0

    while i < n:
        if starts[i] < ends[j]:
            current_overlap += 1
            if current_overlap > max_overlap:
                max_overlap = current_overlap
            i += 1
        else:
            current_overlap -= 1
            j += 1

    return max_overlap