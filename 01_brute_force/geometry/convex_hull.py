def convex_hull(points):
    """Find convex-hull boundary segments by testing pairs of points.
    
    Preconditions:
    For the usual hull-edge interpretation, points must be distinct
    numeric (x, y) pairs with no three collinear; orientation comparisons
    must be exact enough to preserve which side of a line a point lies on.
    
    Result:
    Return unordered boundary segments, not a cyclic vertex ordering.
    With collinear points, also return overlapping supporting segments;
    duplicates may produce zero-length segments. This behavior is retained.
    """
    n = len(points)
    segmentos = []

    for i in range(n):
        for j in range (i+1, n):
            x1 = points[i][0]
            y1 = points[i][1]
            x2 = points[j][0]
            y2 = points[j][1]
            
            a = y2 - y1
            b = x1 - x2
            c = x1*y2 - y1*x2

            menorIgual = True
            maiorIgual = True


            for k in range(n):
                if k != i and k != j:
                    test_c = a*points[k][0] + b*points[k][1]
                    if test_c < c:
                        maiorIgual = False
                    elif test_c > c:
                        menorIgual = False
            if menorIgual or maiorIgual:
                segmentos.append((points[i], points[j]))

    return segmentos