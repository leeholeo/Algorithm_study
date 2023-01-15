'''
누적합
'''
import sys


input = sys.stdin.readline
M, N = map(int, input().split())
accum = [0] * (2*M)
for _ in range(N):
    zero, one, two = map(int, input().split())
    accum[zero] += 1
    accum[zero+one] += 1
hull = [[1] * (2*M - 1)]
now = 0
for i in range(2*M - 1):
    now += accum[i]
    hull[0][i] += now
for depth in range(1, M):
    hull_length = M - depth
    outer_hull = hull[-1]
    upper_inner_hull = outer_hull[-hull_length:]
    left_inner_hull = [upper_inner_hull[0]] * (hull_length-1)
    inner_hull = left_inner_hull + upper_inner_hull
    hull.append(inner_hull)

hive = [[None] * M for _ in range(M)]
for j in range(M):
    for i in range(M-1, 0+j, -1):
        hive[i][j] = hull[j][M-1-i]
    hive[j][j:] = hull[j][-M+j:]

for line in hive:
    print(*line)


# from itertools import accumulate
# import sys
#
#
# M, N = map(int, input().split())
# grow = [0] * (2 * M)
#
# for line in sys.stdin:
#     if line == '\n': break
#     zero, one, two = map(int, line.split())
#
#     grow[zero] += 1
#     grow[zero + one] += 1
#
# grow = list(accumulate([1] + grow))[1:-1]
#
# s = " ".join(str(x) for x in grow[M:])
#
# for i in range(M):
#     print(grow[M - 1 - i], s)