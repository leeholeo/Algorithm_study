'''
2차원 누적합
'''
import sys
input = sys.stdin.readline
R, C, Q = map(int, input().split())
picture = [[0] * (C+1)] + [[0] + list(map(int, input().split())) for _ in range(R)]
for i in range(1, R+1):
    for j in range(1, C+1):
        picture[i][j] += picture[i-1][j] + picture[i][j-1] - picture[i-1][j-1]

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1
    c1 -= 1
    print((picture[r2][c2] - picture[r2][c1] - picture[r1][c2] + picture[r1][c1]) // ((r2-r1) * (c2-c1)))
