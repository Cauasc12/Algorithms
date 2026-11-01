import math

def distance(point1, point2):
    math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def closest_pair(points):
    points_by_x = sorted(points, key=lambda p: p[0])

    def closest_pair_recursive(points):
        n = len(points)

        mid = n // 2
        mid_x = points[mid][0]

        left_d, left_pair = closest_pair_recursive(points[:mid])
        right_d, right_pair = closest_pair_recursive(points[mid:])

        if  left_d < right_d:
            min_d, best_pair = left_d, left_pair
        else:
            min_d, best_pair = right_d, right_pair

        strip = []
        for p in points:
            if abs(p[0] - mid_x) < min_d:
                strip.append(p)

        strip.sort(key=lambda p: p[1])

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

    return closest_pair_recursive(points_by_x)