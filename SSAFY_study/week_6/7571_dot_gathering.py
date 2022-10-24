'''
1. 정렬해서 중간값: 1개일 때 예외처리
2. 무게중심 찾기: 틀렸습니다.
정수 단위로 잘리기 때문에 일반적으로는 무게중심이 최소거리라 하더라도 중간값과 차이가 있을 수 있다.
'''


import sys


input = sys.stdin.readline
N, M = map(int, input().split())
rows = []
cols = []
for _ in range(M):
    r, c = map(int, input().split())
    rows.append(r)
    cols.append(c)

rows.sort()
cols.sort()

answer = sum(rows[-(M//2):]) - sum(rows[:M//2]) + sum(cols[-(M//2):]) - sum(cols[:M//2])

if len(rows) == 1:
    answer = 0
print(answer)
