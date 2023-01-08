'''
이건 또 재미있는 아이디어네
완전 탐색도, dp도 안 되는 경우
특정 조건을 가정한 경우의 가능 여부를 빠르게 확인할 수 있는 경우
상황을 가정하고, 가능 여부를 판단
이분 탐색을 통해 빠르게 탐색
'''
import sys


def possibility(diff):
    partition = 1
    now = 0
    while now < N:
        maxi = arr[now]
        mini = arr[now]
        while now < N-1:
            now += 1
            maxi = max(maxi, arr[now])
            mini = min(mini, arr[now])
            if maxi - mini > diff:
                break
        else:
            return True
        partition += 1
        if partition > M:
            return False


inpurt = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
maximum = max(arr) - min(arr)
minimum = 0
while maximum > minimum:
    medium = (maximum+minimum)//2
    if possibility(medium):
        maximum = medium
    else:
        minimum = medium + 1
print(maximum)
