# library
class ConvexHull:
    @staticmethod
    def CCW(v1, v2, v3):
        (x1, y1), (x2, y2), (x3, y3) = v1, v2, v3
        return x1 * y2 + x2 * y3 + x3 * y1 - y1 * x2 - y2 * x3 - y3 * x1

    @staticmethod
    def delete_grad(ver_tuple):
        ver_grad, ver_x, ver_y = ver_tuple
        return ver_x, ver_y

    @staticmethod
    def distance(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

    @staticmethod
    def larger_distance(a, b, c):
        return b if ConvexHull.distance(a, b) > ConvexHull.distance(a, c) else c

    @staticmethod
    def pop_bottom_right(vertex):
        max_x, min_y = vertex[0]
        vertexes = []
        for x, y in vertex:
            if y > min_y:
                vertexes.append((x, y))
            elif y == min_y:
                if x > max_x:
                    vertexes.append((max_x, min_y))
                    max_x = x
                else:
                    vertexes.append((x, y))
            else:
                vertexes.append((max_x, min_y))
                max_x = x
                min_y = y

        point = (max_x, min_y)
        return point, vertexes

    @staticmethod
    def arc_sorting(N, point, vertexes):
        # 기울기의 경우에는 0~inf -inf~0 순으로 변하므로 양수와 음수를 나눠서 정렬한다.
        max_x, min_y = point
        gradient_vers_pos = []
        gradient_vers_neg = []
        gradient_vers_inf = []
        for i in range(1, N):
            x, y = vertexes[i]
            dx = x - max_x
            dy = y - min_y
            if dx == 0:
                gradient_vers_inf.append((None, x, y))
                continue
            gradient = dy / dx
            if gradient > 0:
                gradient_vers_pos.append((gradient, x, y))
            else:
                gradient_vers_neg.append((gradient, x, y))
        gradient_vers_pos.sort(reverse=True)
        gradient_vers_neg.sort(reverse=True)
        gradient_vers = [(None, max_x, min_y)] + gradient_vers_neg + gradient_vers_inf + gradient_vers_pos
        return gradient_vers

    @staticmethod
    def graham_scan(point, gradient_vers):
        stack = [point, ConvexHull.delete_grad(gradient_vers.pop())]
        while gradient_vers:
            first = stack[-2]
            second = stack[-1]
            next_ver = ConvexHull.delete_grad(gradient_vers[-1])
            CCW_value = ConvexHull.CCW(first, second, next_ver)
            if CCW_value > 0:
                gradient_vers.pop()
                stack.append(next_ver)
            elif CCW_value == 0:
                gradient_vers.pop()
                stack[-1] = ConvexHull.larger_distance(first, second, next_ver)
            else:
                stack.pop()

        if stack[0] == stack[-1]:
            stack.pop()
        return stack

    @staticmethod
    def endpoint_convex_hull(N, vertex):
        # y좌표가 최소인 정점을 찾는다. 여러 개라면 x좌표가 최대인 정점을 선택한다.
        point, vertexes = ConvexHull.pop_bottom_right(vertex)

        # 각도에 따라 정렬한다. 시작점으로부터 기울기로 판단한다.
        gradient_vers = ConvexHull.arc_sorting(N, point, vertexes)

        # Graham scan
        convex_hull = ConvexHull.graham_scan(point, gradient_vers)

        return convex_hull


class RotatingCalipers:
    @staticmethod
    def CCW(v1, v2, v3):
        (x1, y1), (x2, y2), (x3, y3) = v1, v2, v3
        return x1 * y2 + x2 * y3 + x3 * y1 - y1 * x2 - y2 * x3 - y3 * x1

    @staticmethod
    def square_distance(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

    @staticmethod
    def find_ends(convex_hull):
        min_x, min_y = convex_hull[0]
        max_x, max_y = convex_hull[0]
        left_top_idx = 0
        right_bottom_idx = 0
        for idx, (x, y) in enumerate(convex_hull):
            if x < min_x:
                left_top_idx = idx
                min_x = x
                max_y = y
            elif x == min_x:
                left_top_idx = idx
                max_y = max(y, max_y)
            elif x > max_x:
                right_bottom_idx = idx
                max_x = x
                min_y = y
            elif x == max_x:
                right_bottom_idx = idx
                min_y = min(y, min_y)

        return (left_top_idx, right_bottom_idx)

    @staticmethod
    def cal_vector(N, convex_hull, idx, sign):
        next_idx = (idx + 1) % N
        dx = sign * (convex_hull[next_idx][0]-convex_hull[idx][0])
        dy = sign * (convex_hull[next_idx][1]-convex_hull[idx][1])
        vector = (dx, dy)
        return vector, next_idx

    @staticmethod
    def rotating_calipers(N, idxes, convex_hull):
        max_distance = 0
        start, stop = idxes
        now = start
        opposite = stop
        origin = (0, 0)
        now_flag = True
        opposite_flag = True
        while now_flag or opposite_flag:
            max_distance = max(max_distance, RotatingCalipers.square_distance(convex_hull[now], convex_hull[opposite]))
            now_vector, next_now = RotatingCalipers.cal_vector(N, convex_hull, now, 1)
            opposite_vector, next_opposite = RotatingCalipers.cal_vector(N, convex_hull, opposite, -1)
            is_go_now = RotatingCalipers.CCW(origin, now_vector, opposite_vector)
            if is_go_now >= 0:
                now = next_now
                if now == stop:
                    now_flag = False
            if is_go_now <= 0:
                opposite = next_opposite
                if opposite == start:
                    opposite_flag = False

        return max_distance

    @staticmethod
    def furthest_distance(convex_hull):
        N = len(convex_hull)
        idxes = RotatingCalipers.find_ends(convex_hull)
        return RotatingCalipers.rotating_calipers(N, idxes, convex_hull)
# library end


import sys


input = sys.stdin.readline
C = int(input())
vertexes = [tuple(map(int, input().split())) for _ in range(C)]
convex_hull = ConvexHull.endpoint_convex_hull(C, vertexes)
print(RotatingCalipers.furthest_distance(convex_hull) ** 0.5)


'''
거리가 더 긴 쪽으로 front나 end가 가는 방식
hwj8963님의 풀이
https://www.acmicpc.net/source/44286511
'''
# i, j = 0, 1
# d = d_sqr(i, j)
# d_max = d
# while j < len(hull):
#     di = d_sqr(i + 1, j)
#     dj = d_sqr(i, (j + 1) % len(hull))
#     if dj >= di:
#         d_max = max(d_max, dj)
#         j += 1
#     else:
#         d_max = max(d_max, di)
#         i += 1
# print(math.sqrt(d_max))
