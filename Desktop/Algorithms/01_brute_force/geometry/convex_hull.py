def convex_hull(points):
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