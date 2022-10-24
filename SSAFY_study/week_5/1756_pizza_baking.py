"""
오븐 배열은 위에서 봤을 때의 크기로 정리
도우 배열을 순회하며 이분 탐색으로 위치를 찾고, 해당 위치 아래 깊이의 오븐은 제거
"""
# def binary_search(target, sorted_list):
#     front = len(sorted_list)
#     rear = 0
#     while rear < front:
#         half = (front+rear) // 2
#         if sorted_list[half] < target:
#             rear = half + 1
#         else:
#             front = half
#     return rear

import sys


def binary_search(target, sorted_list, limit):
    front = 0
    if sorted_list[front] < target:
        return -1
    rear = limit
    while rear > front:
        half = (front+rear) // 2
        if sorted_list[half] < target:
            rear = half
        else:
            front = half + 1
    return front - 1


input = sys.stdin.readline
D, N = map(int, input().split())
ovens = list(map(int, input().split()))
min_radius = ovens[0]
for i in range(1, D):
    if ovens[i] < min_radius:
        min_radius = ovens[i]
    else:
        ovens[i] = min_radius

limit = D
for radius in map(int, input().split()):
    if (rtn := binary_search(radius, ovens, limit)) == -1:
        print(0)
        break
    limit = rtn
else:
    print(limit + 1)
