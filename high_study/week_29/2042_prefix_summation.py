import sys


def make_tree(tree):
    # 그냥 인덱스 역순으로 돌면서 자식 노드 두 개 더해서 부모 노드에 넣기
    for idx in range(len(tree)-2, 0, -2):
        tree[idx//2] = tree[idx] + tree[idx+1]


def change(tree, idx, num):
    diff = num - tree[idx]
    # 리프 노드에서 루트 노드로 이동하며 값 변경
    while idx >= 0:
        tree[idx] += diff
        idx = (idx-1) // 2  # 부모 노드로 변경


def summation(tree, start, end, now, left, right):
    # 노드의 구간이 계산 구간에 포함된 경우 더하기
    if start <= left and right <= end:
        return tree[now]
    # 노드의 구간이 계산 구간에서 완전히 벗어난 경우 prunning
    if right < start or left > end:
        return 0
    # 노드의 구간이 계산 구간에 걸쳐 있는 경우 자식 노드 두 개 재귀 호출
    return summation(tree, start, end, (now << 1) + 1, left, (left+right)//2) + \
           summation(tree, start, end, (now << 1) + 2, (left+right)//2 + 1, right)


CHANGE = 1
SUMMATION = 2
input = sys.stdin.readline
N, M, K = map(int, input().split())

# 트리 깊이 구하기
n = N
for cnt in range(N):
    n = n >> 1
    if n == 0:
        break
depth = cnt + 1 if N > (1 << cnt) else cnt

# 세그먼트 트리 생성
segment_tree = [0] * ((1 << (depth+1)) - 1) # 포화 이진 트리 생성
leaf_start = (1 << depth) - 1   # 리프 노드 시작점
leaf_idx = leaf_start
# 리프 노드에 값 채우기
for _ in range(N):
    segment_tree[leaf_idx] = int(input())
    leaf_idx += 1
# 트리 채우기
make_tree(segment_tree)

for _ in range(M+K):
    a, b, c = map(int, input().split())
    b -= 1
    # 변경
    if a == CHANGE:
        change(segment_tree, leaf_start+b, c)
    # 구간 합 계산
    elif a == SUMMATION:
        c -= 1
        print(summation(segment_tree, b, c, 0, 0, (1 << depth) - 1))
