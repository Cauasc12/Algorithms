import math

def distance(point1, point2):
    math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def brute_force(points):
    n = len(points)
    d = float('inf')

    for i in range(n):
        for j in range(i+1, n):
            xi, yi = points[i]
            xj, yj = points[j]
            distancia = math.sqrt((xi-xj)**2 + (yi-yj)**2)
            d = min(d, distancia)
            
    return d

def closest_pair(points):

    points_by_x = sorted(points, key=lambda p: p[0])
    points_by_y = sorted(points, key=lambda p: p[1])

    def closest_pair_recursive(px, py):
        n = len(px)
        if n <= 3:
            return brute_force(points)

        mid = n // 2
        mid_point = px[mid]
        mid_x = px[0]

        left_px = px[:mid]
        right_px = px[mid:]

        left_px_x_count = 0
        for p in left_px:
            if p[0] == mid_x:
                left_px_x_count += 1


        left_py = []
        right_py = []
        current_mid_x_count = 0

        for p in py:
            if p[0] < mid_x:
                left_py.append(p)
            elif p[0] > mid_x:
                right_py.append(p)
            else:
                if current_mid_x_count < left_px_x_count:
                    left_py.append(p)
                    current_mid_x_count += 1
                else:
                    right_py.append(p)

        left_d, left_pair = closest_pair_recursive(left_px, left_py)
        right_d, right_pair = closest_pair_recursive(right_px, right_py)

        if  left_d < right_d:
            min_d, best_pair = left_d, left_pair
        else:
            min_d, best_pair = right_d, right_pair 

        strip = []
        for p in points:
            if abs(p[0] - mid_x) < min_d:
                strip.append(p)

        strip_len = len(strip)
        for i in range(strip_len):
            j = i+1
            while j < strip_len and strip[j][1] - strip[i][ 1] < min_d:
                d = distance(strip[i], strip[j])
                if d < min_d:
                    min_d = d
                    best_pair = (strip[i], strip[j])
                j += 1

        return min_d, best_pair